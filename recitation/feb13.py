
### driver file for Point class
from point import Point

p1 = Point(10,20)
p2 = Point(100,40)
p3 = Point(10,20)

# calls the __str__ method to print the x and y values
print(p1)
print(p2)
print(p3)

print('p1 vs p2: ' + str(p1.is_equal(p2)))
print('p1 vs p3: ' + str(p1.is_equal(p3)))
print('p2 vs p3: ' + str(p2.is_equal(p3)))

### Define a Line class
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __str__(self):
        return 'point 1 is ' + str(self.p1) + ' and point 2 is ' + str(self.p2)

### Write driver code to test the methods in Line class that you have defined.
line1 = Line(10, 20, 30, 40)
print(line1)
