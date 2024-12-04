def count_x_mas(grid: list[list[str]]) -> int:
    """
    Count the number of X-MAS patterns in the grid.
    
    :param grid: A 2D list of characters representing the word search grid.
    :return: The count of X-MAS patterns.
    """
    def is_x_mas(x: int, y: int) -> bool:
        """
        Check if an X-MAS pattern exists with 'A' at the center (x, y).
        
        :param x: The row index.
        :param y: The column index.
        :return: True if an X-MAS pattern is found, False otherwise.
        """
        try:
            # Check diagonals for 'M' and 'S'
            return (
                grid[x][y] == 'A' and
                grid[x - 1][y - 1] == 'M' and
                grid[x + 1][y + 1] == 'S' and
                grid[x - 1][y + 1] == 'M' and
                grid[x + 1][y - 1] == 'S'
            )
        except IndexError:
            # If we go out of bounds while checking, it's not a valid pattern
            return False

    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Traverse the grid, looking for a center 'A' with space for diagonals
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
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