# This solution reads the input from a file named `input.txt`, extracts valid multiplication instructions using a regular expression, calculates their multiplication results, and then sums those results. It handles potential file reading errors and uses type hints for better code readability and maintainability.
import re
from typing import List

def parse_input(file_path: str) -> str:
    """Reads the puzzle input from a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError as e:
        raise RuntimeError(f"Error reading the file at {file_path}: {e}")

def extract_mul_instructions(data: str) -> List[tuple]:
    """Extracts valid mul(X,Y) instructions from the corrupted memory string."""
    # This regex pattern matches strings of the form "mul(X,Y)" where X and Y are 1-3 digit numbers
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    return [(int(x), int(y)) for x, y in matches]

def calculate_multiplication_sum(instructions: List[tuple]) -> int:
    """Calculates the sum of the results of the multiplication instructions."""
    return sum(x * y for x, y in instructions)

def main():
    try:
        # Parse the input
        input_data = parse_input('input/input.txt')
        
        # Extract multiplication instructions
        instructions = extract_mul_instructions(input_data)
        
        # Calculate the sum of the multiplications
        result = calculate_multiplication_sum(instructions)
        
        # Print the final answer
        print(f"The sum of all valid multiplications is: {result}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()