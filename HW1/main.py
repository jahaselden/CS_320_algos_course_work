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

        print('left element:', pattern_list[left])
        print('right element:', pattern_list[right])
        # print('left:', left)
        # print('right:', right)
        # print('removed:', removed)

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


print('example 1:', find_palindrome((1, 2)), 'expected: None') 
print('example 2:', find_palindrome((1, 2, 3, 2, 1)), 'expected: ( 1 2 2 1 )')
print('example 3:', find_palindrome((1, 2, 3, 4)), 'expected: None' )
print('example 4:', find_palindrome((1, 2, 3, 2, 4, 1)), 'expected: ( 1 2 3 2 1 )')
# print('example 5:', find_palindrome((1, 2, 3, 4, 2, 1)), 'expected: ( 1 2 4 2 1 )')
# print('example 6:', find_palindrome(('c', 'i', 'v', 'i', 'c')), 'expected: ( c i i c )')
# print('example 7:', find_palindrome(('a', 1, 2, 2, 1, 'a')), 'expected: ( a 1 2 1 a )')

input8 = tuple("Ma is as selfless as I am")
print(input8)
print('example 8:', find_palindrome(input8), 'expected: ( ? )')

# print('example 9:', find_palindrome("string"), 'expected: None')
# print('example 10:', find_palindrome(["this", "is", "not", "a", "tuple"]), 'expected: None')
# print('example 11: ', find_palindrome(3), 'expected: None')

# input12 = tuple("Able was I ere I saw Elba")
# print(input12)
# print('example 12:', find_palindrome(input12), 'expected: ( ? )')

# input13 = ("Able", "was", "I", "ere", "I", "saw", "Elba")
# print('example 13:', find_palindrome(input13), 'expected: None')
