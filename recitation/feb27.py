# 1. Define a recursive function that takes a positive integer n as a parameter and prints the squares of all the
# numbers between 1 and n in decreasing order.
def func1(n):
    if n == 1:
        print(n)
    else:
        print(n*n)
        func1(n-1)

func1(5)
print("-----------------------")
# 2. Define a recursive function that takes a positive integer n as a parameter and prints the squares of all the
# numbers between 1 and n in increasing order.

def func2(n):
    if n == 1:
        print(n)
    else:
        func2(n-1)
        print(n*n)

func2(5)
print("-----------------------")
# 3. Define a recursive function that takes a positive integer n as a parameter and prints the squares of all the
# even numbers between 1 and n in increasing order.
def func3(n):
    if n == 2:
        print(n*n)
    else:
        func3(n-1)
        if n % 2 == 0:
            print(n*n)

func3(8)
print("-----------------------")

# 4. Define a recursive function that takes a positive integer n as a parameter and returns the product of the all the
# odd numbers between 1 and n.
def func4(n):
    if n == 1:
        return 1
    else:
        if n % 2 != 0:
            return n*func4(n - 1)
        else:
            return func4(n - 1)

print(func4(8))
print("-----------------------")

# 5. Define a recursive function that takes two positive integers n and p as a parameter and returns a list of all
# multiples of p between 1 and n. Order of numbers in the returned list doesn't matter.
def func5(n, p):
    if p > n:
        return []
    else:
        l = func5(n - 1, p)
        if n % p == 0:
            l.append(n)
        return l

print(func5(10, 2))
print("-----------------------")

# 6.Define a recursive function that takes a list of positive integers glist and a positive integer p as a parameter
# and returns the sum of multiples of p in glist.
def func6(glist, p):
    if len(glist) == 0:
        return 0

    i = glist[0]
    l = glist[1:]
    if i % p == 0:
        return i + func6(l, p)
    else:
        return func6(l, p)

print(func6([1,2,3,4,5,6,7,8,9,10], 2))
print(2+4+6+8+10)
print("-----------------------")

# 7.Define a recursive function that takes a list of positive integers glist and returns True if glist contains more
# than 2 even numbers
# [Hint: Think of adding an optional parameter that keeps track of how many even numbers have been seen]

def func7(glist, evens=0):
    if evens > 2:
        return True
    if len(glist) == 0:
        return False
    i = glist[0]
    l = glist[1:]
    if i % 2 == 0:
        evens += 1
        return func7(l, evens)
    else:
        return func7(l, evens)

print(func7([2,3,4,5,6]))
print(func7([2,3,5,6]))

