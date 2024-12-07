# This code includes modifications for Part 2 by adding the `||` concatenation operator to the possible operations. It retains all useful functions and structures from Part 1, ensuring that it can evaluate expressions using addition, multiplication, and now concatenation as well. The solution will correctly calculate the total calibration result by considering all operations.
from typing import List, Tuple
import itertools
import os

def parse_input(filepath: str) -> List[Tuple[int, List[int]]]:
    """Parse the input file into a list of tuples containing target values and lists of numbers."""
    equations = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    target_str, numbers_str = line.split(': ')
                    target = int(target_str)
                    numbers = list(map(int, numbers_str.split()))
                    equations.append((target, numbers))
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return []
    except ValueError as e:
        print(f"Error parsing line: {line}. {e}")
        return []
    return equations

def evaluate_expression(numbers: List[int], operators: List[str]) -> int:
    """Evaluate the expression given numbers and operators, left to right."""
    if not numbers or len(numbers) - 1 != len(operators):
        raise ValueError("Invalid input for evaluation.")
    
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':  # Concatenation operator for Part 2
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_possible(target: int, numbers: List[int]) -> bool:
    """Check if it's possible to reach the target using +, *, and || operators between numbers."""
    num_positions = len(numbers) - 1
    # Generate all combinations of operators
    for operators in itertools.product(['+', '*', '||'], repeat=num_positions):
        try:
            if evaluate_expression(numbers, operators) == target:
                return True
        except ValueError as e:
            print(f"Error during evaluation: {e}")
    return False

def calculate_total_calibration_result(equations: List[Tuple[int, List[int]]]) -> int:
    """Calculate the sum of target values for equations that can be satisfied."""
    total_sum = 0
    for target, numbers in equations:
        if is_possible(target, numbers):
            total_sum += target
    return total_sum

def main():
    # Define the path to the input file
    input_filepath = os.path.join('input', 'input.txt')
    
    # Parse the input file
    equations = parse_input(input_filepath)
    
    # Calculate the total calibration result
    total_result = calculate_total_calibration_result(equations)
    
    # Print the final answer
    print(f"The total calibration result is: {total_result}")

if __name__ == "__main__":
    main()