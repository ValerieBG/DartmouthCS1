# filename: jan30pt2.py
# author:   Valerie Gadapati
# date:     Jan 30, 2023
# purpose:  to learn about return statements

def product_func(n, m):
    return n * m

def larger_num(n, m):
    if n > m:
        return n
    if m > n:
        return m


print(larger_num(product_func(125, 1234), product_func(234, 678)))