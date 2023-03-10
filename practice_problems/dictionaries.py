# 1. Define a function that takes a list glist that contains unique integers as parameter. The function returns a
# dictionary that has the integers in glist as keys and associates each key with its square. For example:
# If glist =[1, 5, 2, 4, -2] then function returns the dictionary {1: 1, 2: 4, 4: 16, 5: 25, -2: 4} [Note: that
# order can be different as you cannot predict the order in which key-value pairs are stored in dictionary]
def func1(glist):
    squares = {}
    for i in glist:
        squares[i] = i**2
    return squares

testlist1 = [1, 5, 2, 4, -2]
print(func1(testlist1))

# 2. Let us now generalize problem 1 (given above): Define a function that takes a list glist that contains unique
# integers, and a function func as parameter (Hint: you used this idea in Lab3 for passing compare functions). The
# function func takes an integer as a parameter and returns some value. The function you define should return a
# dictionary that has the integers in glist as keys and associates each key k with func(k), i.e the value returned by
# func when k is passed as parameter. For example:
# If glist =[1, 5, 2, 4, -2] and func = func2 (defined below) then your function returns the
# dictionary {1: 10, 2: 20, 4: 40, 5: 50, -2: -20} [Note: that order can be different as you cannot predict the order
# in which key-value pairs are stored in dictionary]
def func_1(glist, func):
    dict = {}
    for i in glist:
        dict[i] = func(i)
    return dict

def func2(x):
   return x*10

print(func_1(testlist1, func2))

# 3.  Define a function that takes two dictionaries d1 and d2 as parameters and returns a list of keys that appear in
# only one of the two dictionaries. For example:
#  If d1  = {“a”:1, “b”:3, “c”:4} and d2 = {“b”:6, “c”:4, “d”:5} then your function returns [“a”, “d”] [note: order of
#  elements in the returned list doesn’t matter]
def func3(d1, d2):
    uncommon_keys = []
    if len(d1) >= len(d2):
        longer_d = d1
        shorter_d = d2
    else:
        longer_d = d2
        shorter_d = d1

    for i in longer_d.keys():
        if i not in shorter_d.keys():
            uncommon_keys.append(i)

    for i in shorter_d.keys():
        if i not in uncommon_keys and i not in longer_d.keys():
            uncommon_keys.append(i)

    return uncommon_keys

d1  = {"a":1, "b":3, "c":4}
d2 = {"b":6, "c":4, "d":5}
print(func3(d1, d2))

# 4. Define a function that takes two dictionaries d1 and d2 as parameters and returns a list of keys that appear in
# both the dictionaries.
# For example:
# If d1  = {“a”:1, “b”:3, “c”:4} and d2 = {“b”:6, “c”:4, “d”:5} then your function returns [“c”, “b”] [note: order
# of elements in the returned list doesn’t matter]

def func4(d1, d2):
    common_keys = []

    if len(d1) >= len(d2):
        longer_d = d1
        shorter_d = d2
    else:
        longer_d = d2
        shorter_d = d1

    for i in longer_d.keys():
        if i in shorter_d.keys():  # dont need to use .keys()
            common_keys.append(i)

    return common_keys

d1  = {"a":1, "b":3, "c":4}
d2 = {"b":6, "c":4, "d":5}

print(func4(d1, d2))


# 5. Define a function that takes a dictionary d1 as a parameter and returns a list of lists such that each inner list
# contains keys that have the same associated value in d1.
#  For example:
# If d1  = {“a”:1, “b”:3, “c”:4, “d”:3, “e”:1, “f”: 3}  then your function returns [[“a”, “e”], [“b”, “d”, “f”],
# [“c”]]. [note: order of elements in the returned list and inner lists doesn’t matter]

def func5(d1):
    common_list = []

    for i in d1:
        check = False
        for inner_list in common_list:
            if d1[inner_list[0]] == d1[i]:
                inner_list.append(i)
                check = True

        if not check:
            common_list.append([i])

    return common_list
d1 = {"a": 1, "b": 3, "c": 4, "d": 3, "e": 1, "f": 3}
print(func5(d1))

# func to transform dict to list of lists
def func6(d1):
    lol = []
    j = 0
    for i in d1.keys():
        lol.append([i])
        lol[j].append(d1[i])
        j += 1

    return lol

d1  = {"a":1, "b":3, "c":4, "d":3, "e":1, "f": 3}
# print(func6(d1))
