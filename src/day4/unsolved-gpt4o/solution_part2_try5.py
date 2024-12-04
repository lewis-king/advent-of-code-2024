#Let's create a solution that accurately checks for the X-MAS pattern, where each 'MAS' can be read forwards or backwards, and forms an X shape. We'll ensure that we correctly handle all orientations and directions for the pattern.

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

def is_mas_sequence(grid: list[str], r: int, c: int, dr: int, dc: int) -> bool:
    """Check if there is a 'MAS' sequence starting at (r, c) in the direction (dr, dc)."""
    try:
        return (
            grid[r][c] == 'M' and
            grid[r + dr][c + dc] == 'A' and
            grid[r + 2 * dr][c + 2 * dc] == 'S'
        )
    except IndexError:
        return False

def count_x_mas(grid: list[str]) -> int:
    """Count the number of X-MAS patterns in the word search grid."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # Define the diagonal directions for MAS
    directions = [
        ((-1, -1), (1, 1)),  # Top-left to bottom-right
        ((-1, 1), (1, -1)),  # Top-right to bottom-left
        ((1, -1), (-1, 1)),  # Bottom-left to top-right
        ((1, 1), (-1, -1)),  # Bottom-right to top-left
    ]
    
    # Traverse the grid to find the X-MAS pattern
    for r in range(rows):
        for c in range(cols):
            for (dr1, dc1), (dr2, dc2) in directions:
                if (is_mas_sequence(grid, r, c, dr1, dc1) and is_mas_sequence(grid, r, c, dr2, dc2)) or \
                   (is_mas_sequence(grid, r, c, -dr1, -dc1) and is_mas_sequence(grid, r, c, -dr2, -dc2)):
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

### Key Points:
#1. **Pattern Checking:**
#   - We check both forward and backward directions for 'MAS' sequences.
#
#2. **Comprehensive Direction Handling:**
#   - We handle all four diagonal directions and their reverse to cover all possible X-MAS configurations.
#
#3. **Efficient Boundary Checking:**
#   - The `is_mas_sequence` function safely checks for sequences within the grid bounds.
#
#This solution should accurately count all occurrences of the X-MAS pattern in the grid according to the specified rules.