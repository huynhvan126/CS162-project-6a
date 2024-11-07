# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function that takes as its parameter a list of numbers and returns the max value in the list.
def list_max(lst, index=0):
    """
    Returns the maximum value in a list.
    """
    if index == len(lst) - 1:
        return lst[index]

    # Recursive case: get the max of the rest of the list
    max_of_rest = list_max(lst, index + 1)

    # Return the max of the current element and the max of the rest
    return lst[index] if lst[index] > max_of_rest else max_of_rest