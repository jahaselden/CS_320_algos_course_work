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


def find_palindrome(pattern):

    if not tuple_arg(pattern):
        return None

    length = len(pattern)

    if length <= 2:                 # Returned palindrome must be at least 2 elements 
        return None
    
    pattern_list = list(pattern)    # List conversion allows removal of an element

    left = 0                       
    right = length - 1
    removed = 0

    while left <= right and removed < 1:
        if pattern_list[left] == ' ':
            left += 1

        if pattern_list[right] == ' ':
            right -= 1

        if pattern_list[left] == pattern_list[right]:   # Match? Move inward to next comparison    
            left += 1
            right -= 1
        else:
            if left + 1 == right:       # Remove middle to make palindrome, pattern is even
                del pattern_list[left]
                removed += 1
            elif pattern_list[left + 1] == pattern_list[right]:
                del pattern_list[left]
                removed += 1
            elif pattern_list[left] == pattern_list[right - 1]:
                del pattern_list[right]
                removed += 1
            else:                       # There is no possible palindrome with one removal
                return None

            left += 1
            right -= 1

    if removed == 0:                    # pattern was already a palindrome. remove middle
        del pattern_list[math.floor(length / 2)]

    pattern = tuple(pattern_list)
    return pattern
