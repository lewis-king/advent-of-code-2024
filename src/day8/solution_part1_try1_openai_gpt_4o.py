# This code parses the input file to create a map of antennas, identifies antennas of the same frequency, calculates possible antinode locations, and finally counts the unique antinode positions within the bounds of the map. It includes error handling for file reading and adheres to best practices for Python development.
from typing import List, Tuple, Dict, Set
import os

def parse_input(file_path: str) -> List[List[str]]:
    """Parse the input file and return a 2D list representation of the map."""
    try:
        with open(file_path, 'r') as file:
            return [list(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        raise

def find_antennas(map_data: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    """Find all antennas on the map and group them by frequency."""
    antennas: Dict[str, List[Tuple[int, int]]] = {}
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(antennas: Dict[str, List[Tuple[int, int]]], map_width: int, map_height: int) -> Set[Tuple[int, int]]:
    """Calculate all unique antinode positions created by the antennas."""
    antinodes: Set[Tuple[int, int]] = set()

    for frequency, positions in antennas.items():
        # For each pair of antennas of the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                (x1, y1), (x2, y2) = positions[i], positions[j]

                # Calculate potential antinode positions
                dx = x2 - x1
                dy = y2 - y1

                # Antinode must be twice as far in the same direction
                x3 = x1 - dx
                y3 = y1 - dy
                x4 = x2 + dx
                y4 = y2 + dy

                # Check if the antinodes are within the bounds of the map
                if 0 <= x3 < map_width and 0 <= y3 < map_height:
                    antinodes.add((x3, y3))
                if 0 <= x4 < map_width and 0 <= y4 < map_height:
                    antinodes.add((x4, y4))

    return antinodes

def main():
    # Define the file path relative to the script's location
    file_path = os.path.join(os.path.dirname(__file__), 'input', 'input.txt')

    # Parse the input file
    map_data = parse_input(file_path)

    # Find all antennas on the map
    antennas = find_antennas(map_data)

    # Calculate the width and height of the map
    map_width = len(map_data[0])
    map_height = len(map_data)

    # Calculate all unique antinode positions
    antinodes = calculate_antinodes(antennas, map_width, map_height)

    # Print the number of unique antinode positions
    print(f"Number of unique antinode positions: {len(antinodes)}")

if __name__ == "__main__":
    main()