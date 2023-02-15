# Exercise: coin flip
# Objective: Make use of different results of a function call to take different actions.
#
# Write a loop that simulates flipping a coin 5 times, and prints out “heads” or “tails” after each flip. Use the Python randint function to determine if the outcome of each flip should be heads or tails.
import math
from random import randint

i = 0
while i<5:
    flip = randint(0,1)
    if flip == 1:
        print("heads")
    elif flip == 0:
        print("tails")
    i = i+1

# Exercise: area 51
# Objective: Write a function that returns a value.
#
# First, write a function circle_area51 that computes the area of a circle of radius 51, and returns that area. Call the function and print the result to verify that it works.
#
# Then write a function circle_area that takes a parameter radius, and computes the area o a circle with that radius. Call the function three times, to compute the areas of circles of size 3, 5, and 51, and print the results.

def circle_area51():
    area = math.pi * (51 * 51)  # pi(r^2)
    return area

print(circle_area51())

def circle_area(r):
    area = math.pi * (r * r)
    return area

print(circle_area(3))
print(circle_area(5))
print(circle_area(51))