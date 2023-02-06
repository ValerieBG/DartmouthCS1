# Variables, function definitions, and return statements:
# Define a variable and assign it a value of 100.
x = 100

# Define a variable and assign it any integer value. In the second line define another variable and assign it the value
# of the first variable.
y = 100
z = y
# Define a variable and assign it any integer value. In the next line increment the value of the variable you defined
# by 10.
a = 85
a += 10

# Define a function that prints two lines of message of your choice. Include a call to the function.
def func1():
    print("line 1 of something")
    print("line 2 of something")

func1()

# Define a function that takes a positive integer as a parameter and multiplies it by -1 and prints the result.
# Include a call to the function and pass a value of your choice.
def func2(posInt):
    x = posInt * -1
    print(x)

func2(3)

# Define a function that takes two positive integers as parameters and prints the product of the two parameters.
# Include a call to the function and pass values of your choice.
def func_product(posInt1, posInt2):
    x = posInt1 * posInt2
    print(x)

func_product(3, 4)

# Define a function that takes two positive integers as parameters and prints the smaller of the two parameters.
# Include two calls to your function. In one call the first parameter is smaller than the second and in the second
# call the second parameter is the smaller one. Assume the two parameters will never be equal.
# (Note: this needs you to use if statements)
def func_smaller(posInt1, posInt2):
    if posInt1 > posInt2:
        print(posInt2)
    else:
        print(posInt1)

func_smaller(5, 7)
func_smaller(10, 5)

# Define a function that takes a positive integer as a parameter and multiplies it by -1 and returns the result.
# Include a call to the function and pass a value of your choice. Also include the code to print the value returned by
# the call.
def func3(posInt):
    x = posInt * -1
    return x

num = func3(5)
print(num)

# Define a function, func4, that takes two integers as parameters and returns the sum of the number. Define a function
# func5 that takes two integers as parameters and returns the product of the two numbers. Call func1 and func2 on with
# the same values for parameters. Print the sum of the values returned by the two calls.
def func4(int1, int2):
    sum = int1 + int2
    return sum

def func5(int1, int2):
    product = int1 * int2
    return product

i = func4(3, 4)
j = func5(3, 4)
print(i + j)


# If statements and while loops:

# 1. Define a function that takes an integer n as a parameter and prints n if n is positive and prints 0 if n is
# non-positive (this includes 0).
def func6(n):
    if n > 0:
        print(n)
    else:
        print(0)

# 2. Define a function that takes an integer n as a parameter and prints n if n is positive, prints None if n is 0,
# and prints the square of n (n*n) if n is negative.
def func7(n):
    if n > 0:
        print(n)
    elif n == 0:
        print("None")
    else:
        square = n * n
        print(square)

# 3.  Define a function that takes an positive integer n as a parameter and does the following: 1) prints "even" if n is
# even and "odd" if n is odd. 2) prints "multiple of 5" if n is a multiple of 5, otherwise prints "not a multiple of 5".

def func8(n):
    if n%2 == 0:
        print("even")
    else:
        print("odd")
    if n%5 == 0:
        print("multiple of 5")
    else:
        print("not a multiple of 5")

# 4. Define a function that takes a positive integer n as a parameter and prints all values between 1 and n
# (including 1 and n) in increasing order.
def func9(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

# 5. Define a function that takes a positive integer n as a parameter and prints all values between 1 and n
# (including 1 and n) in decreasing order.
def func10(n):
    i = n
    while i >= 1:
        print(i)
        i -= 1

# 6. Define a function that takes a positive integer n as a parameter and prints all numbers between 1 and n that are
# multiples of 5 or 3, including 1 and n if they satisfy the condition.
def func11(n):
    i = 1
    while i <= n:
        if i % 5 == 0 or i % 3 == 0:
            print(i)
        i += 1
