# 1. Define a function that takes a list of integers glist as parameter and prints the even numbers in glist.
# For example if glist = [1, 4, 5, 20, 2, 12, 81]  then your program should print:
# 4
# 20
# 2
# 12
def func1(glist):
    for i in glist:
        if i%2 == 0:
            print(i)

list_a = [1, 4, 5, 20, 2, 12, 81]
func1(list_a)
print("--------------")

# 2. Define a function that takes a list of integers glist as parameter and prints the numbers at even index.
# For example if glist = [1, 4, 5, 20, 2, 12, 81]  then your program should print:
# 1
# 5
# 2
# 81
def func2(glist):
    i = 0
    while i < len(glist):
        if i % 2 == 0:
            print(glist[i])
        i += 1

list_b = [1, 4, 5, 20, 2, 12, 81]
func2(list_b)
print("--------------")

# 3. Define a function that takes a list of integers glist that is sorted (in increasing order) and an integer n as
# parameters and inserts n into glist in such a way that glist remains sorted.
def func3(glist):
    temp = 0
    for i in glist:
        if i < temp:

# 4. Define a function that takes a list of integers glist as parameter and returns True if the list is either sorted
# in decreasing or increasing order. Otherwise it returns False.
# [Extra practice: If you used two loops, think how you can solve this problem with only one loop.]
#
# 5. Define a function that takes two lists glist1 and glist2 as parameters and returns True if they are the reverse
# of each other, otherwise returns False. For simplicity you can assume that the given lists contain only integers.
#
#
# 1. Define a function that takes a list of integers glist as a parameter and returns a list containing all the even
# numbers in glist. Please note that the function should create a new list and not modify the given list glist.
#
# 2. Define a function that takes a list of integers glist as parameter and returns a list containing those numbers in
# glist that are equal to the index at which they appear in glist. Please note that the function should create a new
# list and not modify the given list glist.
#
# For example:
# If glist = [0, 13, 2, 33, 5, 67, 36, 7] then your function should return [0, 2, 7]
# If glist =[10, 20, 30, 40, 50] then your function should return [ ]
#
# 3. Define a function that takes two lists gl1 and gl2 of integers as parameters. Assume the following:
#   a. Each list has unique numbers. (Note: A number can occur in both lists)
#   b. Both lists are sorted in increasing order
#
# Your function should return a list that is sorted in increasing order and contains the numbers in both the lists.
# But if a number appears in both the lists then it should appear only once in the result list.
# Please note that the function should create a new list and not modify the given lists gl1 and gl2.
#
#
# For example:
# If gl1 = [10, 20, 30, 40] and gl2 = [11, 20, 44, 56, 60] then the result list will be [10, 11, 20, 30, 40, 44, 56, 60]
# If gl1 = [ ] and gl2 = [11, 20, 44] then the result list will be [11, 20, 44]
#
# 4. Define a function that takes two strings gs1 and gs2 as parameters and returns True if the alphabet “a” appears
# an equal number of times in both the strings.
#
# 5. Define a function that takes a list of integers glist as a parameter and swaps the positions of the minimum and
# the maximum number in the list. Assume that the list has unique integers. Please note that your function should not
# create a new list, instead it should change the given list. Assume there is at least one element in the given list.
#
# For example: If glist = [10, 5, -7, 34, 28, 107, -2, 6] then your function should change the given list to
# [10, 5, 107, 34, 28, -7, -2, 6].
