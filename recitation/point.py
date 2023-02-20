#Author: Vasanta
#Date: 02/12/2023
#Purpose: Point class definition

# for use in feb13 recitation

class Point:
    def __init__(self, gx, gy):
        self.x = gx
        self.y = gy

    def is_equal(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True
        else:
            return False

        #Can also be written in one line as
        #return self.x == other_point.x and self.y == other_point.y

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

