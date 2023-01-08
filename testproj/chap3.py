# exercise: even in a range

# use test cases 0, 3, 24, 25, 32, 33, and 34
x = 34

# write a single boolean expression to see if x is even and between 24-32 (inclusive)
print((x % 2 == 0) and (x >= 24) and (x <= 32))

# exercise: count while
# count to 5 and print output as counter increases
x = 0
while x <= 5:
    print(x)
    x = x+1

# exercise: count down
# count down from 100 to 0 by 2's

x = 100
while x >= 0:
    print(x)
    x = x - 2

# exercise: series
# print 1st 100 numbers in the series of numbers 1,2,4,7,11,16,22
x = 1
increase = 1

while increase <= 100:
    print(x)
    x = x + increase
    increase = increase + 1