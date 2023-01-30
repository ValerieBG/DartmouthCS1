# 1. Define a function print_evens that takes a positive integer n as parameter and prints all the even numbers between
# 0 and n, excluding n irrespective of if it is even or odd.
def print_evens(n):
    i = 0
    while i <= n:
        if i%2 == 0:
            print(i)
        i = i + 1
    if n%2 == 1:
        print(n)

# 2. Define a function print_evens2 that takes a positive integer n as parameter and prints all the even numbers between
# 0 and n, including n if it is an even number.
def print_evens2(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            print(i)
        i = i + 1

# 3. Define a function print_odds that takes a positive integer n as parameter and prints all the odd numbers between 0
# and n, including n if it is an odd number.
def print_odds(n):
    i = 0
    while i <= n:
        if i % 2 == 1:
            print(i)
        i = i + 1

# 4. Define a function product_even that takes a positive integer n as parameter and prints the product of all even
# numbers between 1 and n (including n).
def product_even(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            print(i*i)  # unsure what product of all even numbers means...
        i = i + 1

# 5. Define a function product_odd that takes two positive integers m and n as parameters and prints the product of all
# odd numbers between m and n. You may assume m < n and m is odd.
def product_odd(m, n):
    i = m
    while i <= n:
        if i % 2 == 1:
            print(i * i)  # unsure what product of all odd numbers means...
        i = i + 1

# 6. Define a function product_odd that takes two positive integers m and n as parameters and prints the product of all
# odd numbers between m and n. You may assume m < n. Parameters m and n can be even or odd.

# product_odd(2,4) # would be the same as product_odd in my case

# 7. Define a function last_k_evens1 that takes two positive integers n and k as parameters. It should print the last k
# even numbers between 1 and n. You can make the following assumptions:
    # There are at least k even numbers between 1 and n
    # n is an even number

def last_k_evens1(n, k):
    i = n
    j = 0
    while i > 0:
        if j < k:
            if i % 2 == 0:
                print(i)
                j = j + 1
        i = i - 1

# 8. Define a function last_n_evens2 that takes two positive integers n and k as parameters. It should print the last k
# even numbers between 1 and n. You can make the following assumptions:
    # There are at least k even numbers between 1 and n

# would be same as last_n_evens1 for me

# NOTE: see the practice document for test cases for questions 9 through 12
# 9. Define a function last_k_evens3 that takes two positive integers n and k as parameters. Your function should do the following:
    # print the last k even numbers between 1 and n if there are k or more even numbers between 1 and n.
    # Otherwise, it should print all the even numbers between 1 and n.

def last_k_evens3(n, k):
    if k > n//2:
        i = n
        j = 0
        while i > 0:
            if j < k:
                if i % 2 == 0:
                    print(i)
                    j = j + 1
        i = i - 1
    else:
        i = 0
        while i <= n:
            if i % 2 == 0:
                print(i)
            i = i + 1

# 10. Define a function factorial_limit1 that takes a positive integer limit as parameter and prints the largest number
# whose factorial is strictly less than the value limit.

def factorial_limit1(n):
    fact = 1
    i = 1
    while fact < n:
        i = i + 1
        fact = fact * i
    print(i - 1)

# 11. Define a function factorial_limit2 that takes a positive integer limit as parameter and prints the largest number
# whose factorial is less than or equal to limit.

def factorial_limit2(n):
    fact = 1
    i = 1
    while fact <= n:
        i = i + 1
        fact = fact * i
    print(i - 1)

# 12. Define a function lcm that takes two positive integer parameters m and n, and prints the smallest number that is
# divisible by both m and n.

def lcm(m, n):
    i = (m>=n)*m+(n>m)*n # larger of two numbers is starting point
    while i < m*n: # max it would be is m * n
        if i%m == 0 and i%n == 0: # if divisible by both
            return(i) # return it and move on
        else:
            return(m*n) # if none of 1 worked, return the default lcm
        i = i + 1

# 13. Define a function is_factorial, that takes a positive integer n as parameter and prints True if it is a factorial
# of another positive integer. Otherwise it prints False. [Note: Your program should print False or True only once]
def is_factorial(n):
    fact = 1
    i = 1
    while i <= n:
        i = i + 1
        fact = fact * i
        if n == fact:
            return True
    return False

# 14. Define a function gcd that prints the greatest common divisor of two positive integers m and n that are passed as
# parameters to the function.

def gcd(m, n):
    i = min(m, n)  # smaller of two numbers is starting
    while i > 0:
        if m%i == 0 and n%i == 0:
            return i
        i = i - 1
    return i
