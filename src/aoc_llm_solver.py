import os
from pathlib import Path
from enum import Enum
from typing import Literal, Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain.globals import set_debug

set_debug(True)

# Load environment variables
load_dotenv()


class ModelProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"


class AoCLLMSolver:
    def __init__(self,
                 day: int,
                 part: int,
                 provider: ModelProvider = ModelProvider.OPENAI,
                 model_name: str = "gpt-4",
                 part1_solution_path: Optional[Path] = None):
        """
        Initialize the solver with specified model configuration.

        Args:
            day: Day number of the puzzle
            part: Part number of the puzzle (1 or 2)
            provider: The model provider to use (openai or anthropic)
            model_name: The specific model to use
            part1_solution_path: Optional path to part 1 solution file (required for part 2)
        """
        self.day = day
        self.part = part
        self.provider = provider
        self.model_name = model_name
        self.attempt_number = 1

        # Initialize the appropriate LLM based on provider
        if provider == ModelProvider.OPENAI:
            self.llm = ChatOpenAI(model=model_name)
        elif provider == ModelProvider.ANTHROPIC:
            self.llm = ChatAnthropic(model=model_name)
        else:
            raise ValueError(f"Unsupported model provider: {provider}")

        self.output_parser = StrOutputParser()
        self.chat_history = []

        # Create base directory structure
        self.base_dir = Path(__file__).parent.resolve()
        self.day_dir = self.base_dir / f"day{self.day}"
        self.day_dir.mkdir(parents=True, exist_ok=True)

        # Load part 1 solution if solving part 2
        self.part1_solution = None
        if part == 2:
            if not part1_solution_path:
                raise ValueError("Part 1 solution path is required when solving part 2")
            self.part1_solution = self.load_solution(part1_solution_path)

    def load_solution(self, solution_path: Path) -> str:
        """Load a solution from a file."""
        if not solution_path.exists():
            raise FileNotFoundError(f"No solution found at {solution_path}")

        with open(solution_path, "r") as f:
            return f.read()

    def read_puzzle_description(self) -> str:
        """Read the puzzle description from the corresponding day's folder."""
        description_path = self.day_dir / "input" / f"description_part{self.part}.txt"

        if not description_path.exists():
            raise FileNotFoundError(f"No description found for day {self.day} at {description_path}")

        with open(description_path, "r") as f:
            return f.read()

    def read_puzzle_input(self) -> str:
        """Read the puzzle input from the corresponding day's folder."""
        input_path = self.day_dir / "input" / "input.txt"

        if not input_path.exists():
            raise FileNotFoundError(f"No input found for day {self.day} at {input_path}")

        with open(input_path, "r") as f:
            return f.read()

    def save_solution(self, solution: str) -> Path:
        """Save the solution to a file with attempt number and return the path."""
        model_suffix = f"_{self.provider.value}_{self.model_name.replace('-', '_')}"
        solution_path = self.day_dir / f"solution_part{self.part}_try{self.attempt_number}{model_suffix}.py"

        solution_path.parent.mkdir(parents=True, exist_ok=True)

        with open(solution_path, "w", encoding='utf-8') as f:
            f.write(solution)
            f.flush()
            os.fsync(f.fileno())

        return solution_path

    def generate_solution(self) -> str:
        """Generate a Python solution using the LLM."""
        print(f"\nGenerating solution attempt #{self.attempt_number} using {self.provider.value} - {self.model_name}")
        description = self.read_puzzle_description()
        sample_input = self.read_puzzle_input()

        escaped_sample_input = sample_input.replace("{", "{{").replace("}", "}}")

        # Create system message that won't be affected by template variables
        system_message = """You are an expert Python programmer helping to solve Advent of Code puzzles.
            Generate a complete Python solution for the given puzzle description.
            The solution should:
            1. Be well-commented and clearly explain the approach
            2. Include proper error handling
            3. Be efficient and follow Python best practices
            4. Include type hints where appropriate
            5. Parse the input file correctly from 'input/input.txt' relative to the script's location
            6. Print the final answer

            Important: The input file is located at 'input/input.txt' relative to the script.
            Your solution should use this path to read the input file.

            Return only the Python code, no explanations before or after."""

        messages = [("system", system_message)]

        if self.part == 2 and self.part1_solution:
            # Double-escape any curly braces in the solution code
            escaped_solution = self.part1_solution.replace("{", "{{").replace("}", "}}")
            messages.append(("user", f"""Here is the working solution for Part 1:
            ```python
            {escaped_solution}
            ```

            Now, here is Part 2's description (including Part 1 for extra context):
            {description}

            Here is a sample of the input format:
            {escaped_sample_input}

            Please modify the Part 1 solution to solve Part 2. Maintain any useful helper functions and data structures and maintain the ability for the solution to produce the result for both parts.
            Remember to clearly indicate the Part 2 modifications in the comments."""))
        else:
            messages.append(("user", f"""Here is the puzzle description:
            {description}

            Here is a sample of the input format:
            {escaped_sample_input}"""))

        messages.extend([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", f"Please generate a Python solution to solve Part {self.part} of this puzzle.")
        ])

        prompt = ChatPromptTemplate.from_messages(messages)
        chain = prompt | self.llm | self.output_parser
        return chain.invoke({"chat_history": self.chat_history})

    def provide_feedback(self, solution: str, feedback: str) -> str:
        """Provide feedback about a solution attempt and get an improved version."""
        self.chat_history.extend([
            AIMessage(content=f"Here was my solution attempt #{self.attempt_number}:\n```python\n{solution}\n```"),
            HumanMessage(
                content=f"This solution didn't work. Here's what happened: {feedback}\nPlease provide an improved solution that addresses these issues.")
        ])

        self.attempt_number += 1
        return self.generate_solution()


def solve_puzzle(
        day: int,
        part: int,
        provider: ModelProvider = ModelProvider.OPENAI,
        model_name: str = "gpt-4",
        part1_solution_path: Optional[Path] = None
):
    # Validate part number and solution path requirements
    if part not in [1, 2]:
        raise ValueError("Part must be either 1 or 2")
    if part == 2 and not part1_solution_path:
        raise ValueError("Part 1 solution path is required when solving part 2")

    try:
        solver = AoCLLMSolver(
            day=day,
            part=part,
            provider=provider,
            model_name=model_name,
            part1_solution_path=part1_solution_path
        )
    except FileNotFoundError as e:
        if part == 2:
            # Check if the directory exists and list available files
            day_dir = Path(__file__).parent.resolve() / f"day{day}"
            if day_dir.exists():
                print(f"\nError: {e}")
                print("\nAvailable solution files in this directory:")
                for file in day_dir.glob("solution_part1*.py"):
                    print(f"- {file.name}")
                print("\nPlease use one of these filenames when running part 2.")
            else:
                print(f"\nError: No solutions found for day {day}. Please solve part 1 first.")
        raise

    try:
        current_solution = solver.generate_solution()

        while True:
            print(f"\nGenerated Python Solution (Attempt #{solver.attempt_number}):")
            print("-" * 80)
            print(current_solution)
            print("-" * 80)

            solution_path = solver.save_solution(current_solution)
            print(f"\nSolution saved to: {solution_path}")
            print(f"To use this solution for part 2, use the path: {solution_path}")

            print("\nPlease verify the solution has been saved and test it.")
            feedback = input("Did this solution work? If not, please provide feedback (or 'exit' to quit): ")

            if feedback.lower() == 'exit' or feedback.lower() == 'yes':
                break

            current_solution = solver.provide_feedback(current_solution, feedback)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage with different models:
    base_dir = Path(__file__).parent.resolve()
    day = 6
    part = 2
    # Solve Part 1
    #solve_puzzle(day=day, part=part, provider=ModelProvider.OPENAI, model_name="gpt-4o")

    # Solve Part 2 (after completing part 1)
    solve_puzzle(
         day=day,
         part=part,
         provider=ModelProvider.OPENAI,
         model_name="gpt-4o",
         part1_solution_path=base_dir / "day6/solution_part1_try1_openai_gpt_4o.py"
    )