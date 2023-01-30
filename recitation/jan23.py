# define a function that takes a positive integer n and prinbts the sum of all even nums between 1 and n

def even_sum(n):
    i = 0
    total = 0
    while i <= n:
        if i % 2 == 0:
            total = total + i
        i = i + 1

    print(total)

even_sum(20)

# takes an n number of pos int input, print only even evens, and if none are even print 1
def input_evens(n):
    evens = []
    i = 0
    while i < n:
        print("give me a number: ")
        x = int(input())
        if x % 2 == 0:
            evens.append(x)
        i = i + 1
        product = 1
    for j in evens:
        product = product * j
    print(product)

def input_evens_optimized(n):
    i = 0
    product = 1

    while i < n:
        print("give me a number: ")
        x = int(input())
        if x % 2 == 0:
            product = product * x
        i = i + 1
    print(product)

input_evens_optimized(4)