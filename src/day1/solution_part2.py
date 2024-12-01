from collections import Counter
from typing import List, Tuple

def read_input(filename: str) -> Tuple[List[int], List[int]]:
    """
    This function reads the input file which contains two columns of integers.
    It returns two lists of integers.
    """
    left_list = []
    right_list = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
    except FileNotFoundError:
        print("Input file not found.")
        return left_list, right_list
    
    return left_list, right_list


def calculate_similarity_score(left_list: List[int], right_list: List[int]) -> int:
    """
    This function calculates the similarity score by counting how often 
    each number from the left list appears in the right list.
    It then adds up each number in the left list after multiplying it by the number of times 
    that number appears in the right list.
    """
    similarity_score = 0
    right_list_counter = Counter(right_list)
    
    for number in left_list:
        similarity_score += number * right_list_counter[number]
    
    return similarity_score

def main():
    left_list, right_list = read_input('input/input.txt')
    print(calculate_similarity_score(left_list, right_list))

if __name__ == "__main__":
    main()