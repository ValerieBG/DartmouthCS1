# filename: counterTest.py
# author:   Valerie Gadapati
# date:     Feb 6, 2023
# purpose:  file to test the counter class

from counter import *

# create first test counter
testCounter1 = Counter(10, 5, 4)

i = 0
while i <= 10:
    print(testCounter1, str(testCounter1.tick()))  # prints value and whether it wrapped
    i = i + 1

print("-------------")

# create another test counter, this one to test the initial value out of range
testCounter2 = Counter(5, 8, 2)

j = 0
while j <= 15:
    print(testCounter2)
    testCounter2.tick()
    j = j + 1

# make sure get_value() function works
print("current val as int: ", testCounter2.get_value())
