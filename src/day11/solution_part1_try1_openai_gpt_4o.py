#This Python script reads the initial configuration of stones from an input file, processes the transformations over 25 blinks according to the rules provided, and outputs the total number of stones after all transformations. The code includes error handling for file operations and parsing, ensuring robustness against common errors.
def read_input(file_path: str) -> list[int]:
    """Reads the input file and returns a list of integers representing the stones."""
    try:
        with open(file_path, 'r') as file:
            # Read the single line, strip whitespace, and convert each number to an integer
            return list(map(int, file.readline().strip().split()))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except ValueError as e:
        print(f"Error parsing the input: {e}")
        raise

def evolve_stones(stones: list[int], blinks: int) -> list[int]:
    """Evolves the stones according to the given rules for a specified number of blinks."""
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                # Split the number into two halves
                digits = str(stone)
                half_len = len(digits) // 2
                left_half = int(digits[:half_len])
                right_half = int(digits[half_len:])
                new_stones.extend([left_half, right_half])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return stones

def main():
    # Set up the path to the input file
    input_file_path = 'input/input.txt'
    
    # Read the initial stones from the input file
    try:
        stones = read_input(input_file_path)
    except Exception as e:
        print(f"Failed to read and parse input: {e}")
        return
    
    # Number of blinks
    blinks = 25
    
    # Evolve the stones for the given number of blinks
    final_stones = evolve_stones(stones, blinks)
    
    # Print the number of stones after 25 blinks
    print(f"Number of stones after {blinks} blinks: {len(final_stones)}")

if __name__ == "__main__":
    main()