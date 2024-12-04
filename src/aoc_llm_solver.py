import os
from pathlib import Path
from enum import Enum
from typing import Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

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
                 model_name: str = "gpt-4"):
        """
        Initialize the solver with specified model configuration.

        Args:
            day: Day number of the puzzle
            part: Part number of the puzzle (1 or 2)
            provider: The model provider to use (openai or anthropic)
            model_name: The specific model to use
                For OpenAI: "gpt-4", "gpt-4-turbo-preview", etc.
                For Anthropic: "claude-3-opus-20240229", "claude-3-sonnet-20240229", etc.
        """
        self.day = day
        self.part = part
        self.provider = provider
        self.model_name = model_name

        # Initialize the appropriate LLM based on provider
        if provider == ModelProvider.OPENAI:
            self.llm = ChatOpenAI(model=model_name)
        elif provider == ModelProvider.ANTHROPIC:
            self.llm = ChatAnthropic(model=model_name)
        else:
            raise ValueError(f"Unsupported model provider: {provider}")

        self.output_parser = StrOutputParser()
        self.chat_history = []
        self.attempt_number = 1

        # Create base directory structure
        self.base_dir = Path(__file__).parent.resolve()
        self.day_dir = self.base_dir / f"day{self.day}"
        self.day_dir.mkdir(parents=True, exist_ok=True)

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
        # Include model info in filename for better tracking
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

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert Python programmer helping to solve Advent of Code puzzles.
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

            Return only the Python code, no explanations before or after."""),
            ("user", f"""Here is the puzzle description:
            {description}

            Here is a sample of the input format:
            {escaped_sample_input}  # Only show first 200 chars of input as example

            You are currently solving Part {self.part}. Remember to read the input from 'input/input.txt'."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "Please generate a Python solution to solve this puzzle.")
        ])

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


def main(day: int, part: int, provider: ModelProvider = ModelProvider.OPENAI, model_name: str = "gpt-4"):
    solver = AoCLLMSolver(day=day, part=part, provider=provider, model_name=model_name)

    try:
        current_solution = solver.generate_solution()

        while True:
            print(f"\nGenerated Python Solution (Attempt #{solver.attempt_number}):")
            print("-" * 80)
            print(current_solution)
            print("-" * 80)

            solution_path = solver.save_solution(current_solution)
            print(f"\nSolution saved to {solution_path}")

            print("\nPlease verify the solution has been saved and test it.")
            feedback = input("Did this solution work? If not, please provide feedback (or 'exit' to quit): ")

            if feedback.lower() == 'exit' or feedback.lower() == 'yes':
                break

            current_solution = solver.provide_feedback(current_solution, feedback)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Example usage with different models:

    # For OpenAI GPT-4o
    main(4, 2, ModelProvider.OPENAI, "gpt-4o")

    # For OpenAI GPT-4 Turbo
    # main(4, 2, ModelProvider.OPENAI, "gpt-4-turbo-preview")

    # For Anthropic Claude 3 Sonnet
    # main(4, 2, ModelProvider.ANTHROPIC, "claude-3-5-sonnet-latest")

    # For Anthropic Claude 3 Opus
    # main(4, 2, ModelProvider.ANTHROPIC, "claude-3-opus-20240229")