# filename: counterTest.py
# author:   Valerie Gadapati
# date:     Feb 6, 2023
# purpose:  file to test the counter class

from counter import *

testCounter1 = Counter(10, 5, 4)

i = 0
while i <= 10:
    print(testCounter1, str(testCounter1.tick()))
    i = i + 1

print("-------------")

testCounter2 = Counter(5, 2, 2)

j = 0
while j <= 15:
    print(testCounter2, testCounter2.tick())
    j = j + 1

print(testCounter2.get_value())
