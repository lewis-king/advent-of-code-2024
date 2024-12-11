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
    
    # Part 1: Number of blinks is 25
    blinks_part_1 = 25
    final_stones_part_1 = evolve_stones(stones, blinks_part_1)
    print(f"Part 1 - Number of stones after {blinks_part_1} blinks: {len(final_stones_part_1)}")
    
    # Part 2: Number of blinks is 75
    blinks_part_2 = 75
    final_stones_part_2 = evolve_stones(stones, blinks_part_2)
    print(f"Part 2 - Number of stones after {blinks_part_2} blinks: {len(final_stones_part_2)}")

if __name__ == "__main__":
    main()