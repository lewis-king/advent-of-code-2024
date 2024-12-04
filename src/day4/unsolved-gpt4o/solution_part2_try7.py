#Let's solve the problem by carefully identifying the X-MAS pattern as described: two "MAS" sequences forming an X shape, where each "MAS" can be either forwards or backwards. We'll ensure that we consider all possible orientations.

#Here is the solution:

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

def is_mas(grid: list[str], r: int, c: int, dr: int, dc: int) -> bool:
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

    # Directions for the two MAS in the X shape
    diagonals = [
        ((-1, -1), (1, 1)),  # Top-left to bottom-right
        ((-1, 1), (1, -1)),  # Top-right to bottom-left
    ]

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            for (dr1, dc1), (dr2, dc2) in diagonals:
                # Check for the X-MAS pattern
                if is_mas(grid, r, c, dr1, dc1) and is_mas(grid, r, c, dr2, dc2):
                    count += 1
                # Also check the reverse pattern
                if is_mas(grid, r, c, -dr1, -dc1) and is_mas(grid, r, c, -dr2, -dc2):
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

### Key Elements of the Solution:
#1. **Input Reading:**
#   - Read each line from the input file and store it as a list of strings representing the grid.

#2. **Pattern Detection:**
#   - We create a function `is_mas` to check if there is a "MAS" sequence in a specified direction.

#3. **Direction Handling:**
#   - We define two diagonals that need to be checked for the pattern, accounting for both forward and backward directions.

#4. **Pattern Counting:**
#   - Traverse each cell in the grid and check for the X-MAS pattern using the defined diagonals. Count each occurrence found.

#This solution should provide the correct count for the X-MAS pattern in the grid. It ensures thorough checking across all potential configurations of the pattern.