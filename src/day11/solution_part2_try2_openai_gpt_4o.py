### Explanation:
# **Optimization with `Counter`:** Instead of maintaining a list of stones, which can become very large, we use a `Counter` from Python's `collections` module to keep track of the number of each type of stone. This allows us to efficiently handle large numbers of stones.
# **Efficiency:** By tracking counts of stone types, we reduce the amount of data we need to process at each step, which significantly improves performance for a large number of blinks.
# **Functionality:** The script reads the input, processes the stones for a given number of blinks, and prints the results for both Part 1 and Part 2.

def read_input(file_path: str) -> list[int]:
    """Reads the input file and returns a list of integers representing the stones."""
    try:
        with open(file_path, 'r') as file:
            return list(map(int, file.readline().strip().split()))
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except ValueError as e:
        print(f"Error parsing the input: {e}")
        raise

def evolve_stones_optimized(stones: list[int], blinks: int) -> int:
    """Evolves the stones according to the given rules for a specified number of blinks."""
    from collections import Counter

    # Using a Counter to track the count of each stone type
    stone_counts = Counter(stones)

    for _ in range(blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                digits = str(stone)
                half_len = len(digits) // 2
                left_half = int(digits[:half_len])
                right_half = int(digits[half_len:])
                new_stone_counts[left_half] += count
                new_stone_counts[right_half] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts

    # Return the total number of stones
    return sum(stone_counts.values())

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
    num_stones_part_1 = evolve_stones_optimized(stones, blinks_part_1)
    print(f"Part 1 - Number of stones after {blinks_part_1} blinks: {num_stones_part_1}")
    
    # Part 2: Number of blinks is 75
    blinks_part_2 = 75
    num_stones_part_2 = evolve_stones_optimized(stones, blinks_part_2)
    print(f"Part 2 - Number of stones after {blinks_part_2} blinks: {num_stones_part_2}")

if __name__ == "__main__":
    main()