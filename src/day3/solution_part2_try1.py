# This solution reads the corrupted memory from an input file, and then scans through it character by character. It uses regular expressions to match the valid instructions defined in the puzzle description. When it encounters a do() instruction, it enables future multiplications, and when it encounters a don't() instruction, it disables them. For each mul() instruction it encounters while multiplications are enabled, it multiplies the two numbers and adds the result to a sum. Finally, it prints the sum of all the results.
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
    for i in range(len(corrupted_memory)):
        # Check for do() and don't() instructions
        if do_regex.match(corrupted_memory[i:i+5]):
            mul_enabled = True
        elif dont_regex.match(corrupted_memory[i:i+7]):
            mul_enabled = False

        # If multiplications are enabled, check for mul() instructions
        if mul_enabled:
            mul_match = mul_regex.match(corrupted_memory[i:i+9])
            if mul_match:
                # Multiply the two numbers and add them to the sum
                num1, num2 = map(int, mul_match.groups())
                result += num1 * num2

    return result

def main():
    corrupted_memory = read_file('input/input.txt')
    result = sum_enabled_multiplications(corrupted_memory)
    print(f'The sum of the results of the enabled multiplications is {result}.')

if __name__ == "__main__":
    main()
