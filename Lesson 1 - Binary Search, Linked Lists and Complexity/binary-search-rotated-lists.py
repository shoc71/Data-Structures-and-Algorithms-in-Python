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

Safe to assume that all numbers in the list will be unique.
'''
# imports
import random

# global variables
test_cases = [
    {'input' : {'nums' : [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output' : 3},
    {'input' : {'nums' : [4, 5, 6, 7, 8, 1, 2, 3]}, 'output' : 5},
    {'input' : {'nums' : [50, 90, 100, 110, 120, 140, 160]}, 'output' : 0},# no rotation
    {'input' : {'nums' : [3, 5, 7, 1]}, 'output' : 1,},
    {'input' : {'nums' : []}, 'output' : 0}, # empty list
    {'input' : {'nums' : [1]}, 'output' : 0}, # no rotation
    {'input' : {'nums' : [86, 43, 43, 37, 34, 32, 13]}, 'output' : 6,}, # n-1 rotation, n=len(list)
    {'input' : {'nums' : [10, 12, 14, 23, 53, 55, 57, 59, 2]}, 'output' : 8,},
    {'input' : {'nums' : [32, 35, 36, 37, 58, 61]}, 'output' : 0} # len(list) rotated, n = len(list) times
]

def number_list_sorted(list_of_numbers):
    return sorted(list_of_numbers)

def covering_edge_cases(lst: list) -> bool:
    return len(lst) <= 1

def brute_force_count_rotations(nums: list):
    '''
    Argument:
        list of rotated sorted numbers

    Returns:
        count (int) of rotations of the sorted list
    '''
    if covering_edge_cases(nums):
        return 0
        
    pos = 0
    while True:
        # print(nums[pos])
        if nums[pos - 1] < nums[pos]:
            pos += 1
        else:
            return f"Rotation of sorted list: {pos}"

def binary_count_rotations(nums: list):
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        middle_number = nums[middle]

        if middle > 0:
            return middle
        
        elif middle <0:
            high = middle - 1

        else:
            low = middle + 1

    return 0



for index in range(len(test_cases)):
    print(test_cases[index]['input'])
    print(brute_force_count_rotations(test_cases[index]['input']['nums']))