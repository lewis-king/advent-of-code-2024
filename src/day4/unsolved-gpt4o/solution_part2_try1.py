# This code reads the input from a file, checks for the X-MAS pattern in all possible directions, and counts the number of occurrences. It handles errors that may occur during file reading and ensures efficient and clear processing of the word search grid.
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

    # Define the X-MAS pattern directions: two MAS in an X shape
    directions = [
        ((-1, -1), (1, 1)),  # Top-left to bottom-right
        ((-1, 1), (1, -1)),  # Top-right to bottom-left
        ((1, -1), (-1, 1)),  # Bottom-left to top-right
        ((1, 1), (-1, -1)),  # Bottom-right to top-left
    ]

    # Check if the MAS pattern exists starting from (r, c)
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
            if grid[r][c] == 'M':  # Check for the start of a MAS
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