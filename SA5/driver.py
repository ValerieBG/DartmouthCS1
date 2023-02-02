# filename: driver.py
# author:   Valerie Gadapati
# date:     Feb 6, 2023
# purpose:  create a class that makes a digital counter

from counter import *

testCounter = Counter(10, 5, 4)
i = 0
while i <= 10:
    print(testCounter)
    testCounter.tick()
    i = i + 1