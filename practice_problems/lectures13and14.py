# 1. Define a function that takes a list of lists glol as parameter.  You may assume that each inner list inside glol
# is a list of integers. For example: [[1, 2], [10, 20], [30, 10], [-4, -5]].
# Your function returns True if at least one list inside glol is sorted in increasing order and at least one list is
# sorted in decreasing order, else it returns False.
def eval(listy):
    i = 1
    inc = 0
    dec = 0
    while i < len(listy):
        if listy[i-1] < listy[i]:
            inc += 1
        if listy[i-1] > listy[i]:
            dec += 1
        i += 1
    return inc == len(listy) - 1 or dec == len(listy)

def func1(glol):
    incordec = 0
    for elem in glol:
        incordec += int(eval(elem))
    return incordec == 2

f1_test1 = [[2, 3, 4], [4, 3, 2], [3, 9]]
f1_test2 = [[2, 5, 4], [3, 4, 5], [3, 7, 4]]

print(func1(f1_test1))
print(func1(f1_test2))

# 2. Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set of
# characters that occur with the same frequency (you are checking if s1 and s2 are anagrams). For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return False
def func2(s1, s2):
    s1_map = []
    for char in s1:
        if char in s1_map:
            s1_map[char] += 1
        else:
            s1_map[char] = 1
    # Check if the frequency map of s1 is the same as the frequency map of s2
    for char in s2:
        if char not in s1_map:
            return False
        elif s1_map[char] == 0:
            return False
        else:
            s1_map[char] -= 1
    # Check if all characters in s1_map have a frequency of 0
    for char in s1_map:
        if s1_map[char] != 0:
            return False
    # If all tests passed, the strings are anagrams
    return True

print(func2("dirtyroom", "dormitory"))
print(func2("dirty room", "dormitory"))

# 3. Define a function that takes two strings s1 and s2 as parameters and checks if they have the same set of
# characters but possibly with a different frequency. For example:
# If s1 = “dirtyroom” and s2 = “dormitory” then it should  return True
# If s1 = “dirty room” and s2 = “dormitory” then it should return False (space is counted as a character)
# If s1 = “too” and s2 = “to” then it should return True


# 4. Define a function that takes a list of lists as a parameter such that each inner list is a list of integers. The
# function should return a list containing all integers that occur only in one of the inner lists. For example:
#  If the given list is [[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]] then the function should return
#  [12, -10,  60]
# If the given list is [[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]] then the function should
# return []
# You can assume that all numbers within any inner list are unique.
# But the same number can appear in multiple inner lists.


# 5. Define a function that takes a list of positive integers (greater than 0) as a parameter and returns a list of
# lists. Your  function should group the numbers based on the number of digits they have. Each inner list in the
# returned list represents one such group. Also, in the returned list the inner lists should be sorted in order of
# length of the numbers they contain. You are not allowed to sort the given list.
# For example:
#  If the given list is [9, 67, 200, 456, 20023, 3, 10, 999] then it should return
#  [[9, 3], [67, 10], [200, 456, 999], [20023]]
# If the given list is [] then it should return []


# 6. Define a function that takes a list of positive integers glist as parameter and returns a list of lists.
# Assume len(glist) > 0. The returned list of lists should satisfy the following conditions:
#   Each inner list in the returned list contains numbers from glist that can form a sequence of consecutive numbers.
#   Only longest sequence/sequences should be added to the returned list (there can be multiple longest sequences,
#   see example 2 below)
#   The order of numbers in inner lists does not matter.
#   The order of inner lists in the returned list does not matter.
#   Assume the list has unique numbers.
#
#
# For example:
# If glist = [100, 8, 9, 3, 99, 2, 101], then your function should return [[99, 100, 101]].
# If glist = [ 8, 12,  9, 3, 99, 2, 101], then your function should return [[2, 3], [9, 8]].
# If glist = [ 8, 2, 10], then your function should return [[8], [2], [10]] as the longest consecutive sequences are
# all of length 1 (i.e. the individual elements).
#
#
# You are not allowed to sort the given list or sort any list created using the given list.