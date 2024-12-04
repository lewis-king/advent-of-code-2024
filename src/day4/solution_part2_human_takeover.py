def count_x_mas(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Iterate over each possible center of the 'X' (the 'A' position)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                left_down_right = grid[row-1][col-1] + grid[row+1][col+1]
                right_down_left = grid[row-1][col+1] + grid[row+1][col-1]
                if ((left_down_right == 'SM' or left_down_right == 'MS') and
                        (right_down_left == 'SM' or right_down_left == 'MS')):
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
    input_file_path = './input/input.txt'
    grid = read_input(input_file_path)

    if not grid:
        return

    result = count_x_mas(grid)
    print(f"The number of X-MAS patterns is: {result}")

if __name__ == "__main__":
    main()
