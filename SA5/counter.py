# filename: counter.py
# author:   Valerie Gadapati
# date:     Feb 6, 2023
# purpose:  define a class that counts down

class Counter:
    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit
        self.initial = initial
        self.min_digits = min_digits

        # If the initial value supplied as a parameter is between 0 and limit–1 then that's the counter's initial value
        if 0 <= initial < (limit - 1):
            self.count = initial
        # otherwise an error message is printed and the counter's initial value is limit–1.
        else:
            print("Error: initial value outside countdown range")
            self.count = limit - 1

    # returns the counter's value as a string with the number of digits min_digits specifies
    # zeroes are padded to the left as needed (e.g. 15 turns to 0015 if min_digits is 4)
    def __str__(self):
        if len(str(self.count)) < self.min_digits:
            return (self.min_digits - len(str(self.count))) * '0' + str(self.count)
        else:
            return str(self.count)

    # returns the counter's value, as an int.
    def get_value(self):
        return self.count

    # decrements the counter's value, but if the value would go negative, then it wraps around to limit–1.
    # returns a boolean value indicating whether it wrapped around
    def tick(self):
        if self.count - 1 < 0:
            self.count = self.limit - 1
            wrapped = True
        else:
            self.count = self.count - 1
            wrapped = False
        return wrapped
