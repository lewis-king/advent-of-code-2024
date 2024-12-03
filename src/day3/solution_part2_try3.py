import re

def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return ''

def sum_enabled_multiplications(corrupted_memory: str) -> int:
    # Regular expressions to find valid instructions
    mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_regex = re.compile(r'do\(\)')
    dont_regex = re.compile(r'don\'t\(\)')

    # Initialize the sum and flag for enabled multiplications
    result = 0
    mul_enabled = True

    # Iterate over the corrupted memory
    i = 0
    while i < len(corrupted_memory):
        # Check for do() and don't() instructions
        do_match = do_regex.search(corrupted_memory[i:])
        dont_match = dont_regex.search(corrupted_memory[i:])
        mul_match = mul_regex.search(corrupted_memory[i:])

        # Find the nearest instruction
        do_index = do_match.start() if do_match else float('inf')
        dont_index = dont_match.start() if dont_match else float('inf')
        mul_index = mul_match.start() if mul_match else float('inf')
        min_index = min(do_index, dont_index, mul_index)

        # If there are no more instructions, break the loop
        if min_index == float('inf'):
            break

        # Process the nearest instruction
        if min_index == do_index:
            mul_enabled = True
            i += do_match.end()
        elif min_index == dont_index:
            mul_enabled = False
            i += dont_match.end()
        else:
            if mul_enabled:
                # Multiply the two numbers and add them to the sum
                num1, num2 = map(int, mul_match.groups())
                result += num1 * num2
            i += mul_match.end()

    return result

def main():
    corrupted_memory = read_file('input/input.txt')
    result = sum_enabled_multiplications(corrupted_memory)
    print(f'The sum of the results of the enabled multiplications is {result}.')

if __name__ == "__main__":
    main()