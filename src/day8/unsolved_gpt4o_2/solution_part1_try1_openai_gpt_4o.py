# This code reads an input file containing a map of antennas, identifies the positions of antennas, and calculates unique antinode locations based on the given conditions. It handles potential errors like file not found and ensures that calculations consider the bounds of the map. The final output is the count of unique antinode locations.
from typing import List, Tuple, Set
import os

def parse_input(file_path: str) -> List[str]:
    """Reads the input file and returns the content as a list of strings."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")

def find_antennas(map_data: List[str]) -> List[Tuple[int, int, str]]:
    """Finds all antennas in the map and returns their positions and frequencies."""
    antennas = []
    for y, line in enumerate(map_data):
        for x, char in enumerate(line):
            if char != '.':
                antennas.append((x, y, char))
    return antennas

def calculate_antinodes(antennas: List[Tuple[int, int, str]], width: int, height: int) -> Set[Tuple[int, int]]:
    """Calculates all unique antinodes in the map."""
    antinodes = set()
    # Group antennas by frequency
    frequency_map = {}
    for x, y, freq in antennas:
        if freq not in frequency_map:
            frequency_map[freq] = []
        frequency_map[freq].append((x, y))
    
    # Calculate antinodes for each frequency
    for freq, positions in frequency_map.items():
        positions.sort()  # Sort by x first, then by y if x is the same
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                (x1, y1) = positions[i]
                (x2, y2) = positions[j]
                
                # Check for perfect horizontal or vertical alignment
                if x1 == x2 or y1 == y2:
                    # Calculate midpoint and distance
                    mx, my = (x1 + x2) // 2, (y1 + y2) // 2
                    dx, dy = x2 - x1, y2 - y1
                    
                    # Ensure one is twice as far as the other
                    if dx % 2 == 0 and dy % 2 == 0:
                        # Calculate potential antinodes
                        antinode1 = (x1 - dx // 2, y1 - dy // 2)
                        antinode2 = (x2 + dx // 2, y2 + dy // 2)

                        # Add antinodes if they are within bounds
                        if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                            antinodes.add(antinode1)
                        if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                            antinodes.add(antinode2)

    return antinodes

def main():
    # Define the path to the input file
    file_path = os.path.join(os.path.dirname(__file__), 'input', 'input.txt')
    
    # Parse the input data
    map_data = parse_input(file_path)
    
    # Determine map dimensions
    height = len(map_data)
    width = len(map_data[0]) if height > 0 else 0
    
    # Find all antennas
    antennas = find_antennas(map_data)
    
    # Calculate all unique antinodes
    antinodes = calculate_antinodes(antennas, width, height)
    
    # Print the number of unique antinode locations
    print(len(antinodes))

if __name__ == "__main__":
    main()