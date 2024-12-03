import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()


class AoCLLMSolver:
    def __init__(self, day: int, part: int):
        self.day = day
        self.part = part
        self.llm = ChatOpenAI(model="gpt-4")
        self.output_parser = StrOutputParser()
        self.chat_history = []  # Store the conversation history

    def read_puzzle_description(self) -> str:
        """Read the puzzle description from the corresponding day's folder."""
        current_dir = Path(__file__).parent
        description_path = current_dir / f"day{self.day}/input/description_part{self.part}.txt"

        if not description_path.exists():
            raise FileNotFoundError(f"No description found for day {self.day} at {description_path}")

        with open(description_path, "r") as f:
            return f.read()

    def read_puzzle_input(self) -> str:
        """Read the puzzle input from the corresponding day's folder."""
        current_dir = Path(__file__).parent
        input_path = current_dir / f"day{self.day}/input/input.txt"

        if not input_path.exists():
            raise FileNotFoundError(f"No input found for day {self.day} at {input_path}")

        with open(input_path, "r") as f:
            return f.read()

    def generate_solution(self) -> str:
        """Generate a Python solution using the LLM."""
        print("Reading puzzle description")
        description = self.read_puzzle_description()
        print("Reading puzzle input")
        sample_input = self.read_puzzle_input()

        print("Creating prompt")
        escaped_sample_input = sample_input[:200].replace("{", "{{").replace("}", "}}")

        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert Python programmer helping to solve Advent of Code puzzles.
            Generate a complete Python solution for the given puzzle description.
            The solution should:
            1. Be well-commented and clearly explain the approach
            2. Include proper error handling
            3. Be efficient and follow Python best practices
            4. Include type hints where appropriate
            5. Parse the input file correctly
            6. Print the final answer

            Return only the Python code, no explanations before or after."""),
            ("user", f"""Here is the puzzle description:
            {description}

            Here is a sample of the input format:
            {escaped_sample_input}  # Only show first 200 chars of input as example

            You are currently solving Part {self.part}."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "Please generate a Python solution to solve this puzzle.")
        ])

        chain = prompt | self.llm | self.output_parser
        print("Generating solution")
        return chain.invoke({"chat_history": self.chat_history})

    def provide_feedback(self, solution_output: str, feedback: str) -> str:
        """Provide feedback about a solution attempt and get an improved version."""
        # Add the previous solution attempt and feedback to chat history
        self.chat_history.extend([
            AIMessage(content=f"Here was my previous solution attempt:\n```python\n{solution_output}\n```"),
            HumanMessage(
                content=f"This solution didn't work. Here's what happened: {feedback}\nPlease provide an improved solution that addresses these issues.")
        ])

        # Generate a new solution with the updated chat history
        return self.generate_solution()


def main(day: int, part: int):
    solver = AoCLLMSolver(day=day, part=part)

    try:
        # Initial solution attempt
        solution = solver.generate_solution()
        while True:
            print("Generated Python Solution:")
            print("-" * 80)
            print(solution)
            print("-" * 80)

            current_dir = Path(__file__).parent
            solution_path = current_dir / f"day{solver.day}/solution_part{solver.part}.py"
            solution_path.parent.mkdir(parents=True, exist_ok=True)

            with open(solution_path, "w") as f:
                f.write(solution)
            print(f"\nSolution saved to {solution_path}")

            # Ask for feedback
            feedback = input("\nDid this solution work? If not, please provide feedback (or 'exit' to quit): ")
            if feedback.lower() == 'exit' or feedback.lower() == 'yes':
                break

            # Generate improved solution based on feedback
            solution = solver.provide_feedback(solution, feedback)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main(3, 2)