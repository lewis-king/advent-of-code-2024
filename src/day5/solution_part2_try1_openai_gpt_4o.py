# This solution reads the input from the specified file, determines which updates are not in the correct order using the provided rules, reorders them using a topological sort when necessary, and calculates the sum of the middle pages of these correctly ordered updates. The code includes error handling for file operations and ensures only relevant rules are considered for each update.
from typing import List, Tuple, Set
import os

def read_input(file_path: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """Reads the input file and returns the rules and updates."""
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
        
        sections = content.split('\n\n')
        rules = [tuple(map(int, line.split('|'))) for line in sections[0].strip().split('\n')]
        updates = [list(map(int, line.split(','))) for line in sections[1].strip().split('\n')]
        
        return rules, updates
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found at: {file_path}")
    except ValueError:
        raise ValueError("Error processing input file. Ensure the file format is correct.")

def is_correct_order(rules: List[Tuple[int, int]], update: List[int]) -> bool:
    """Checks if the update is in the correct order according to the rules."""
    position_map = {page: i for i, page in enumerate(update)}
    
    for x, y in rules:
        if x in position_map and y in position_map:
            if position_map[x] >= position_map[y]:
                return False
    return True

def order_update(rules: List[Tuple[int, int]], update: List[int]) -> List[int]:
    """Orders the update according to the rules using topological sort."""
    from collections import defaultdict, deque

    # Build graph and in-degree count
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    # Only consider rules that are relevant for the current update
    relevant_rules = [(x, y) for x, y in rules if x in update and y in update]

    for x, y in relevant_rules:
        if y not in graph[x]:
            graph[x].add(y)
            in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0

    # Apply topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update

def solve_part_two(file_path: str) -> int:
    """Solves part two of the puzzle."""
    rules, updates = read_input(file_path)
    incorrect_updates_middle_sum = 0

    for update in updates:
        if not is_correct_order(rules, update):
            ordered = order_update(rules, update)
            middle_page = ordered[len(ordered) // 2]
            incorrect_updates_middle_sum += middle_page

    return incorrect_updates_middle_sum

if __name__ == "__main__":
    input_file_path = 'input/input.txt'
    result = solve_part_two(input_file_path)
    print(f"Sum of middle pages of correctly ordered updates: {result}")