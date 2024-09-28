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
numbered_list = []
test_case = {}

# generating test cases
for loop in range(7):
    numbered_list.append(random.randint(0,100))

numbered_list_sorted = sorted(numbered_list)

def covering_edge_cases(lst: list) -> bool:
    return len(lst) <= 1

def count_rotations(nums: list):
    pass

print(numbered_list_sorted)