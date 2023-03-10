# 1. Define a function that takes the head of a linked list hnode and integers val1 and val2 as parameters. Your
# function should replace every occurrence of val1 as data in a given linked list by val2. Assume that the data stored
# in each node is an integer.
def func1(hnode, val1, val2):
    new_list = []
    return new_list


# 2.  Define a function that takes the head of a linked list as a parameter. Assume that the data stored in each node
# is an integer. Your function returns the maximum data in the linked list.
# For example: The given linked list is:  10 → 15 → 2→ 30 → -10 → 5 then it should return 30

def func2(hnode):
    n = hnode
    max = n.data
    while n != None:
        if n.data >= max:
            max = n.data
        n = n.next
    return max

# 3. Define a function that takes the head of a linked list as a parameter. Assume that the data stored in each node is
# an integer. Your function should return the sum of all the integers stored as data in the nodes of the linked list.
# For example: The given linked list is:  10 → 15 → 2→ 30 → -10 → 5 then it should return  52

# 4. Define a function insert_before that takes the head of a linked list, and two integers val_before and val as
# parameters. Assume that the data stored in each node is an integer. Your function should insert a new node with
# data as val such that the next node of the new node is the first node in the given  linked list with data as
# val_before. You may assume that a node with data val_before will always exist in the given linked list. For example:
# If the given head is reference to head node the linked list:
# 10 → 15 → 2→ 30 → 10 → 5, val_before is 10 and val is 20, then after adding the node the linked list should
# \be 20 → 10 → 15 → 11→ 2→ 30 → 10 → 5.
# If the given head is reference to head node the linked list:
# 10 → 15 → 2→ 30 → -10 → 5, val_before is 2 and val is 11, then after adding the node the linked list should
# be 10 → 15 → 11→ 2→ 30 → -10 → 5.

