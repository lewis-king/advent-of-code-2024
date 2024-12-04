def count_x_mas(grid: list[list[str]]) -> int:
    """
    Count the number of X-MAS patterns in the grid.
    
    :param grid: A 2D list of characters representing the word search grid.
    :return: The count of X-MAS patterns.
    """
    def is_x_mas(x: int, y: int) -> bool:
        """
        Check if an X-MAS pattern exists starting at (x, y).
        
        :param x: The row index.
        :param y: The column index.
        :return: True if an X-MAS pattern is found, False otherwise.
        """
        try:
            # Check the 'X' pattern for "MAS"
            return (
                grid[x][y] == 'M' and
                grid[x + 1][y + 1] == 'A' and
                grid[x + 2][y + 2] == 'S' and
                grid[x + 2][y] == 'M' and
                grid[x + 1][y + 2] == 'A' and
                grid[x][y + 2] == 'S'
            )
        except IndexError:
            # If we go out of bounds while checking, it's not a valid pattern
            return False

    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Traverse the grid, allowing space for the 3x3 X-MAS pattern
    for i in range(rows - 2):
        for j in range(cols - 2):
            if is_x_mas(i, j):
                count += 1

    return count

def read_input(file_path: str) -> list[list[str]]:
    """
    Read the input file and convert it into a 2D list grid.
    
    :param file_path: The path to the input file.
    :return: A 2D list representing the grid.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Strip each line and convert it to a list of characters
            return [list(line.strip()) for line in lines]
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    # Read the grid from the input file
    file_path = 'input/input.txt'
    grid = read_input(file_path)

    if grid:
        # Count and print the number of X-MAS patterns
        result = count_x_mas(grid)
        print(f"The number of X-MAS patterns found is: {result}")
    else:
        print("No grid data available to process.")

if __name__ == "__main__":
    main()