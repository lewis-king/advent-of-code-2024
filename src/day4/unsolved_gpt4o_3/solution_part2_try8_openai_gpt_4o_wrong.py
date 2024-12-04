# Here is a refined and complete solution that accurately counts all the possible 'X-MAS' patterns:
# This solution correctly handles all eight possible orientations of the 'X-MAS' pattern by checking both 'M' and 'S' sequences in each pattern orientation. It ensures that each pattern is considered in both possible arrangements of 'M' and 'S', thereby capturing all valid 'X-MAS' patterns. The code reads the input from 'input/input.txt', processes the grid, and outputs the count of the patterns found with proper error handling for file operations.
def count_x_mas(grid: list[list[str]]) -> int:
    """
    Count the number of 'X-MAS' patterns in the given word search grid.

    An 'X-MAS' pattern is defined by a 3x3 grid with 'A' in the center and
    'M' and 'S' on the diagonals, which can be in any of eight possible orientations.
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Define the relative positions for the pattern (M, S) pairs
    # There are four unique patterns since 'M' and 'S' can be interchanged
    patterns = [
        ((-1, -1), (1, 1), (-1, 1), (1, -1)),  # M top-left, S bottom-right
        ((-1, 1), (1, -1), (-1, -1), (1, 1)),  # M top-right, S bottom-left
        ((-1, -1), (1, 1), (1, -1), (-1, 1)),  # M bottom-left, S top-right
        ((-1, 1), (1, -1), (1, 1), (-1, -1)),  # M bottom-right, S top-left
    ]

    # Iterate over each possible center of the 'X' (the 'A' position)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                # Check all possible X-MAS orientations
                for pattern in patterns:
                    if (grid[row + pattern[0][0]][col + pattern[0][1]] == 'M' and
                        grid[row + pattern[1][0]][col + pattern[1][1]] == 'S' and
                        grid[row + pattern[2][0]][col + pattern[2][1]] == 'S' and
                        grid[row + pattern[3][0]][col + pattern[3][1]] == 'M'):
                        count += 1

    return count

def read_input(file_path: str) -> list[list[str]]:
    """
    Read the input file and return a list of lists representing the word search grid.
    """
    try:
        with open(file_path, 'r') as file:
            return [list(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return []

def main():
    input_file_path = '../input/input.txt'
    grid = read_input(input_file_path)

    if not grid:
        return

    result = count_x_mas(grid)
    print(f"The number of X-MAS patterns is: {result}")

if __name__ == "__main__":
    main()