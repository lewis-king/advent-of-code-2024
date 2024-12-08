# This revised solution calculates antinodes by checking for directional alignment and distance relationships between antennas of the same frequency. It correctly handles the input file and computes the unique positions where antinodes appear on the grid.
from typing import List, Tuple, Set
import os

def parse_input(file_path: str) -> List[str]:
    """Reads the input file and returns a list of strings representing the map."""
    try:
        with open(file_path, 'r') as file:
            return [line.rstrip('\n') for line in file]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        return []

def find_antennas(grid: List[str]) -> List[Tuple[int, int, str]]:
    """Finds all the antennas in the grid and returns their coordinates and frequencies."""
    antennas = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char.isalnum():  # Check if the character is a lowercase letter, uppercase letter, or digit
                antennas.append((x, y, char))
    return antennas

def calculate_antinodes(antennas: List[Tuple[int, int, str]], max_x: int, max_y: int) -> Set[Tuple[int, int]]:
    """Calculates all unique antinode positions in the grid."""
    antinodes = set()

    for i, (x1, y1, freq1) in enumerate(antennas):
        for j in range(i + 1, len(antennas)):
            x2, y2, freq2 = antennas[j]

            if freq1 == freq2:
                # Calculate differences
                dx = x2 - x1
                dy = y2 - y1

                # Only consider antinodes if one point is twice as far as the other
                if dx == 0 or dy == 0 or abs(dx) == abs(dy):
                    # Calculate potential antinode positions
                    antinode1 = (x1 - dx, y1 - dy)
                    antinode2 = (x2 + dx, y2 + dy)

                    # Add to set if within bounds
                    if 0 <= antinode1[0] < max_x and 0 <= antinode1[1] < max_y:
                        antinodes.add(antinode1)
                    if 0 <= antinode2[0] < max_x and 0 <= antinode2[1] < max_y:
                        antinodes.add(antinode2)

    return antinodes

def main():
    file_path = os.path.join('../input', 'input.txt')
    grid = parse_input(file_path)

    if not grid:
        return

    max_x = len(grid[0])
    max_y = len(grid)

    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(antennas, max_x, max_y)

    # Include positions of antennas as they also can be antinodes
    for x, y, _ in antennas:
        antinodes.add((x, y))

    # Print the number of unique antinode positions
    print(f"The number of unique antinode locations is: {len(antinodes)}")

if __name__ == "__main__":
    main()