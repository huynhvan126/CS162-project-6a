# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function that takes as its parameter a list of numbers and returns the max value in the list.
def list_max(numbers):
    """
    Returns the maximum value in a list.
    """
    if len(numbers) == 1:
        return numbers[0]

    # Recursive case: get the max of the rest of the list
    max_of_rest = list_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest
