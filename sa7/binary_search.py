# binary_search.py
# Code provided for CS 1 Short Assignment 7.
# Performs binary search on a sorted list of random numbers.

from random import randint


# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.
def binary_search(the_list, key, left=None, right=None):
    # If using the default parameters, then search the entire list.
    if left is None and right is None:
        left = 0
        right = len(the_list) - 1

    # YOU FILL IN THE REST OF THIS FUNCTION.

    # Compute midpoint of sublist by averaging left and right
    midpoint = (left + right) // 2
    print("midpoint is index", midpoint, " value is", the_list[midpoint])
    print("right index:", right, "; left index:", left)

    # If sublist from index left to index right (inclusive) is empty, key will not be there so return None
    sublist = the_list[left:right]
    if not sublist or right < left:  # 'not list' is same as 'list == False', aka 'list == []', which is an empty list
        return None
    # If key is found in the item at index midpoint of the_list, return midpoint index
    if key == the_list[midpoint]:
        return midpoint
    # Note: the_list is sorted in increasing order
    # if key is in the first half of the sublist, search there using recursion
    if key < the_list[midpoint]:
        # starting at index left and going up to and including the index just before midpoint
        return binary_search(the_list, key, left, midpoint)
    # otherwise search the second half of the list using recursion
    else:
        # starting at the index just after midpoint and going up to and including index right
        return binary_search(the_list, key, midpoint+1, right+1)


# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))
