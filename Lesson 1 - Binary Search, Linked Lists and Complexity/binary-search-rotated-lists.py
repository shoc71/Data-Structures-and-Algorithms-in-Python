'''
You are given list of numbers, obtained by rotating a sorted list an unknown number
of times. 

Write a function to determine the minimum number of times the original sorted list
was rotated to obtain the given list. 

(Your function should have the worst-case complexity of O(log N), where N is the 
length of the list. You can assume that all the numbers in the list are unique.)

[5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list 
[0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it
before the first element. E.g. rotating the list [3, 2, 4, 1] produces 
[1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing 
order e.g. [1, 3, 5, 7]

There can be repeatable numbers.
'''

# def number_list_sorted(list_of_numbers):
#     return sorted(list_of_numbers)

def edge_case_confirmed(lst: list) -> bool:
    return len(lst) <= 1

def count_rotations_brute_force(nums: list):
    '''
    Argument:
        list of rotated sorted numbers

    Returns:
        count (int) of rotations of the sorted list
    '''
    if edge_case_confirmed(nums):
        return 0
        
    pos = 0
    while True:
        # print(nums[pos])
        if nums[pos - 1] < nums[pos]:
            pos += 1
        else:
            # return f"Rotation of sorted list: {pos}"
            return pos

def count_rotations_binary(numbered_list: list):
    '''
        Argument:
            list of rotated sorted numbers

        Returns:
            count (int) of rotations of the sorted list
        '''
    if edge_case_confirmed(numbered_list):
        return 0

    low = 0
    high = len(numbered_list) - 1

    while low <= high:
        # already sorted, not rotated (safe assumption to make, no repeat and duplicates)
        if numbered_list[low] <= numbered_list[high]:
            return low

        middle = (low + high) // 2
        next_idx = (middle + 1) % len(numbered_list)
        prev_idx = (middle - 1 + len(numbered_list)) % len(numbered_list)

        # check if middle is smallest
        if (numbered_list[middle] <= numbered_list[prev_idx]) and (numbered_list[middle] <= numbered_list[next_idx]):
            return middle
        
        # search only right or left half
        if numbered_list[middle] <= numbered_list[high]:
            high = middle - 1
        else:
            low = middle + 1

    return 0


def searching_for_smallest_number(numbered_list, index):

    try:
        list_number_index = numbered_list[index]
        print(f'index: {index} ; current_number: {list_number_index}')
        number_to_right = numbered_list[index + 1]
        number_to_left = numbered_list[index - 1]
    except:
        list_number_index = numbered_list[index -1]
        print(f'index: {index} ; current_number: {list_number_index}')
        number_to_right = numbered_list[index]
        number_to_left = numbered_list[index - 2]

    print(f"number to left : {number_to_left} ; number to right : {number_to_right}\n")
    if (list_number_index < number_to_left) and (list_number_index < number_to_right):
        return 'found'
    
    if (list_number_index < number_to_left) and (list_number_index > number_to_right):
        return 'left'
    else:
        return 'right'

def counting_rotations_using_binary (numbered_list: list[int]):

    if edge_case_confirmed(numbered_list):
        return 0

    low, high = 0, len(numbered_list) - 1

    while low <= high:
        
        middle_index = (low + high) // 2
        print(f"low: {low} ; high: {high} ; middle_index: {middle_index}\n")
        result = searching_for_smallest_number(numbered_list, middle_index)

        if result == 'found':
            return numbered_list[middle_index]
        
        # cutting the list in half in a specific direction
        elif result == 'left':
            high = middle_index - 1

        else: 
            low = middle_index + 1

    
# global variables
test_cases = [
    {'input' : {'nums' : [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output' : 3},
    {'input' : {'nums' : [4, 5, 6, 7, 8, 1, 2, 3]}, 'output' : 5},
    {'input' : {'nums' : [50, 90, 100, 110, 120, 140, 160]}, 'output' : 0},# no rotation
    {'input' : {'nums' : [3, 5, 7, 1]}, 'output' : 1,},
    {'input' : {'nums' : []}, 'output' : 0}, # empty list
    {'input' : {'nums' : [1]}, 'output' : 0}, # no rotation
    {'input' : {'nums' : [86, 43, 40, 37, 34, 32, 13]}, 'output' : 1,}, # n-1 rotation, n=len(list)
    {'input' : {'nums' : [10, 12, 14, 23, 53, 55, 57, 59, 2]}, 'output' : 1,},
    {'input' : {'nums' : [32, 35, 36, 37, 58, 61]}, 'output' : 0} # len(list) rotated, n = len(list) times
]

# test case 4 and 7, continously throw errors 

# Running the test cases
for index, test_case in enumerate(test_cases):
    input_list = test_case['input']['nums']
    expected_output = test_case['output']
    result = counting_rotations_using_binary(input_list)
    assert result == expected_output, f"Test case {index + 1} failed: expected {expected_output}, got {result}"
    print(f"Test case {index + 1} passed. Input: {input_list}, Output: {result}")