#This solution reads the topographic map from a file, identifies trailheads, and computes the score for each trailhead by performing a depth-first search to track all valid hiking trails that reach a height of 9. The total of these scores is then printed as the final answer.
from typing import List, Tuple
import os

def read_input(file_path: str) -> List[List[int]]:
    """Read the input file and return the topographic map as a 2D list of integers."""
    try:
        with open(file_path, 'r') as file:
            return [[int(char) for char in line.strip()] for line in file]
    except FileNotFoundError:
        raise Exception(f"Input file not found at path: {file_path}")
    except ValueError:
        raise Exception("Input file contains non-integer values.")

def is_valid_position(x: int, y: int, map_height: int, map_width: int) -> bool:
    """Check if the given position is within the bounds of the map."""
    return 0 <= x < map_height and 0 <= y < map_width

def find_hiking_trails(map_: List[List[int]], start_x: int, start_y: int) -> int:
    """Find all hiking trails starting from a given trailhead and return the score."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    map_height = len(map_)
    map_width = len(map_[0])
    trail_ends = set()

    def dfs(x: int, y: int):
        """Depth-first search to explore hiking trails."""
        if map_[x][y] == 9:
            trail_ends.add((x, y))
            return
        current_height = map_[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_position(nx, ny, map_height, map_width) and map_[nx][ny] == current_height + 1:
                dfs(nx, ny)

    dfs(start_x, start_y)
    return len(trail_ends)

def calculate_total_score(map_: List[List[int]]) -> int:
    """Calculate the total score of all trailheads in the topographic map."""
    total_score = 0
    for x in range(len(map_)):
        for y in range(len(map_[x])):
            if map_[x][y] == 0:  # trailhead
                total_score += find_hiking_trails(map_, x, y)
    return total_score

def main():
    input_file_path = os.path.join(os.path.dirname(__file__), 'input', 'input.txt')
    topographic_map = read_input(input_file_path)
    total_score = calculate_total_score(topographic_map)
    print(f"The sum of the scores of all trailheads is: {total_score}")

if __name__ == "__main__":
    main()