### DOCUMENTATIOJN UP EHRE




class Counter:
    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit

        # If the initial value supplied as a parameter is between 0 and limit–1, then that's the counter's initial
        # value. Otherwise, an error message is printed and the counter's initial value is limit–1.
        if 0 < initial < limit - 1:
            self.initial = initial
        else:
            print("Error: initial value outside countdown range")
            self.initial = limit - 1
        self.min_digits = min_digits

    # returns the counter's value, as an int.
    def get_value(self):
        return self

    # returns the counter's value, as a string. If the counter's value would print with fewer than the min_digits
    # parameter supplied to the __init__ method, then the string contains min_digits characters, padded on the left with
    # zeros.
    # For example, if min_digits is 4 and the counter's value is 15, then the method should return the string 0015.
    def __str__(self):
        if len(str(self)) < self.min_digits:
            return (self.min_digits - str(self)) * '0' + self
        else:
            return self

    # decrements the counter's value, but if the value would go negative, then it becomes limit–1.
    # For example, if the counter's limit is 12 and its current value is 0, then after calling tick, the counter's
    # value should be 11. This method also returns to its caller a boolean value indicating whether it wrapped around,
    # i.e., did the value wrap from 0 back to limit–1. True means that it wrapped, False means that it did not.
    def tick(self):
        wrapped = False
        self = self - 1
        if self < 0:
            self = self.limit - 1
            wrapped = True
        return wrapped

