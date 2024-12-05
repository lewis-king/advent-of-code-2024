# This code follows the puzzle's description and effectively handles parsing the input, checking the order of updates, and computing the sum of middle page numbers for correctly-ordered updates. It includes error handling for file operations and input parsing, ensuring that the program gracefully reports errors.
from typing import List, Tuple, Set
import os

def parse_input(file_path: str) -> Tuple[Set[Tuple[int, int]], List[List[int]]]:
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    
    parts = content.split('\n\n')
    if len(parts) != 2:
        raise ValueError("Input file does not contain the expected two sections separated by an empty line.")
    
    # Parse ordering rules
    ordering_rules = set()
    for line in parts[0].strip().splitlines():
        if '|' not in line:
            raise ValueError(f"Invalid rule format: {line}")
        x, y = map(int, line.split('|'))
        ordering_rules.add((x, y))
    
    # Parse updates
    updates = []
    for line in parts[1].strip().splitlines():
        update = list(map(int, line.split(',')))
        updates.append(update)
    
    return ordering_rules, updates

def is_valid_order(update: List[int], ordering_rules: Set[Tuple[int, int]]) -> bool:
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in ordering_rules:
        if x in index_map and y in index_map:
            if index_map[x] >= index_map[y]:
                return False
    return True

def find_middle_number(update: List[int]) -> int:
    middle_index = len(update) // 2
    return update[middle_index]

def main():
    input_file_path = os.path.join('input', 'input.txt')
    try:
        ordering_rules, updates = parse_input(input_file_path)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return
    
    correct_order_sum = 0
    for update in updates:
        if is_valid_order(update, ordering_rules):
            middle_number = find_middle_number(update)
            correct_order_sum += middle_number
    
    print("Sum of middle page numbers for correctly-ordered updates:", correct_order_sum)

if __name__ == "__main__":
    main()