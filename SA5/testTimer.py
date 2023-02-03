# filename: timerTest.py
# author:   Valerie Gadapati
# date:     Feb 6, 2023
# purpose:  file to test the timer class

from timer import *

# create a 1 hr 30 min timer
testTimer1 = Timer(1, 30, 0)

# until the timer reaches zero, print the value and count down
while not testTimer1.is_zero():
    print(testTimer1)
    testTimer1.tick()

print(testTimer1)  # print final value w string formatting
