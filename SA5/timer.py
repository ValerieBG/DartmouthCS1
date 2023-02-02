# filename: timer.py
# author:   Valerie Gadapati
# date:     Feb 6, 2023
# purpose:  define a class that creates a 24-hour hours:minutes:seconds timer that counts down

from counter import *

class Timer:

    # creates a timer whose initial values for its hours, minutes, and seconds are given by the parameters.
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    # returns a string giving the timer's current time, in the format hh:mm:ss
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    # function to tick down the timer by one second
    def tick(self):
        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    # function that returns a boolean that is True if the timer currently reads 00:00:00.
    # could i use the wrapped boolean??
    def is_zero(self):
        return self.hours == 0 and self.minutes == 0 and self.minutes == 0
