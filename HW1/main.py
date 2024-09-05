# Determine if a tuple can be made into a palindrome by removing exactly one element

# An example import. Delete or replace as desired. Be careful with what libraries you use:
# Non-default python libraries may not work in Zybooks.
import math 

# Subroutines if any, go here


def tuple_arg(input):
    if isinstance(input, tuple):
        return True
    else:
        return False


def delete_element(tuple, index):
    new_tuple = tuple[:index] + tuple[index + 1:]
    return new_tuple


def find_palindrome(pattern):

    if not tuple_arg(pattern):
        return None

    length = len(pattern)

    if length <= 2:                 # Returned palindrome must be at least 2 elements 
        return None

    left = 0                       
    right = length - 1
    removed = 0
    delete = None

    while left <= right and removed < 1:
        if pattern[left] == pattern[right]:   # Match? Move inward to next comparison    
            left += 1
            right -= 1
        else:
            if left + 1 == right:       # Remove middle to make palindrome, pattern is even
                delete = left
            elif pattern[left + 1] == pattern[right]:
                delete = left
            elif pattern[left] == pattern[right - 1]:
                delete = right
            else:                       # There is no possible palindrome with one removal
                return None         # this isn't returning none!? maybe??
            
            removed += 1

    if removed == 0:                    # Pattern was already a palindrome, remove middle
        delete = math.floor(length / 2)

    pattern = delete_element(pattern, delete)
    return pattern
