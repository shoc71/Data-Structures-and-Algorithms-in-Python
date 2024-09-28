'''
Alice has some cards with some numbers written on them. She arranges
the cards in decreasing order, and lays them out face down in a sequence
on a table. She challenges Bob to pick out the card containing a given 
number by turning over as few cards as possible. 

Write a function to help Bob locate his card.
'''

import random

numbered_list_1 = []
numbered_list_2 = []

for x in range(10_000_000):
    numbered_list_1.append(random.randint(-100, 100))

for x in range(4000):
    numbered_list_2.append(random.randint(-100, 100))

numbered_list_sorted = sorted(numbered_list_1, reverse=True)
chosen_number = random.choice(numbered_list_2)
# chosen_number = 2

# print(chosen_number)
# print(numbered_list_sorted)

def brute_force_locate_number(desired_number: int, list_of_numbers: list[int]):
    index = 0

    # if list does not contain any cards
    if len(list_of_numbers) == 0:
        return -1
    
    while True:
        if desired_number == list_of_numbers[index]:
            return index
        else:
            index += 1
            if index == len(list_of_numbers):
                return -1
            

def special_list_check(list_of_numbers: list[int]) -> bool:
    # Check if the list is empty
    return len(list_of_numbers) == 0
    
def out_of_index_check(list_of_numbers: list[int], index: int) -> bool:
    # Check if the index is out of bounds
    return index >= len(list_of_numbers) or index < 0

def middle_check_locate_number(desired_number: int, list_of_numbers: list[int]):

    # Check for an empty list
    if special_list_check(list_of_numbers):
        return -1
    
    # Initialize pointers for binary search
    left = 0
    right = len(list_of_numbers) - 1
    
    # Continue searching while there are elements to check
    while left <= right:
        index = (left + right) // 2
        # print(f"Index: {index} - Number in list: {list_of_numbers[index]} - Special Number:{desired_number}")

        if desired_number == list_of_numbers[index]:
            return index
        elif desired_number > list_of_numbers[index]:
            right = index - 1  # Search in the left half
        else:
            left = index + 1   # Search in the right half
    
    # If the desired number was not found
    return -1

number_found = middle_check_locate_number(chosen_number, numbered_list_sorted)

print(f"You have {len(numbered_list_sorted):,d} cards to choose from.\n"
    f"Your card is located in {number_found:,d} in the draw.")