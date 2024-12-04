### Explanation of the Solution:
#
#1. **Reading Input:**
#   - The `read_input` function reads the puzzle input from the specified file path and returns it as a list of strings.
#
#2. **Pattern Recognition:**
#   - The `count_x_mas` function counts the occurrences of the X-MAS pattern within the grid.
#   - It checks for two MAS sequences forming an X shape in all four diagonal directions.
#
#3. **Direction Handling:**
#   - The `directions` list contains tuples representing the direction vectors needed to detect the MAS patterns in different diagonal configurations.
#
#4. **Boundary Checking:**
#   - The `is_mas` helper function checks if a MAS sequence can be formed starting from a given position in a specified direction while handling potential IndexError exceptions.
#
#5. **Pattern Counting:**
#   - The grid is traversed, and for each cell, the function checks if it forms the start of an X-MAS pattern, incrementing the count accordingly.
#
#6. **Execution:**
#   - The script reads the grid from `input/input.txt`, processes the grid to count the patterns, and outputs the result.
def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of strings representing the word search."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def count_x_mas(grid: list[str]) -> int:
    """Count the number of X-MAS patterns in the word search grid."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # Define the X-MAS pattern directions
    directions = [
        ((-1, -1), (1, 1)),  # Top-left to bottom-right
        ((-1, 1), (1, -1)),  # Top-right to bottom-left
        ((1, -1), (-1, 1)),  # Bottom-left to top-right
        ((1, 1), (-1, -1)),  # Bottom-right to top-left
    ]

    # Check if the MAS pattern exists starting from (r, c) in the given direction
    def is_mas(r: int, c: int, dr: int, dc: int) -> bool:
        try:
            return (grid[r][c] == 'M' and
                    grid[r + dr][c + dc] == 'A' and
                    grid[r + 2 * dr][c + 2 * dc] == 'S')
        except IndexError:
            return False

    # Traverse the grid to find the X-MAS pattern
    for r in range(rows):
        for c in range(cols):
            for (dr1, dc1), (dr2, dc2) in directions:
                if is_mas(r, c, dr1, dc1) and is_mas(r, c, dr2, dc2):
                    count += 1

    return count

def main():
    input_file = '../input/input.txt'
    grid = read_input(input_file)
    
    if not grid:
        return

    result = count_x_mas(grid)
    print(f"The number of X-MAS patterns found is: {result}")

if __name__ == '__main__':
    main()
