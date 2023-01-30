# Without running the programs, find out what each of the following programs will print?
# If the program gives an error then please mark the line that gives the error.
'''
# 1
def func1():
   print("In func1")
   print("test")

func1()
# In func1
# test

# 2
def func1():
   print("In func1")
   print("test1")

func1()
print("test2")
func1()
# In func1
# test1
# test2
# In func1
# test1

# 3
def func1():
    print("In func1")
func1()
def func2():
    print("In func2")

func2()
func1()

# In func1
# In func2
# In func1

# 4
def func1():
   print("In func1")
func1()

def func2():
   func1()
   print("In func2")

func2()
func1()

# In func1
# In func1
# In func2
# In func1

# 5
def func1():
   func2() # because of this not being defined
   print("In func1")

func1() # would cause error
def func2():
   print("In func2")

func2()

# 6
def func1(p1):
   print("In func1", p1)

func1(10)

# In func1 10

# 7
def func1(p1):
   func2(p1)
   print("In func1", p1)

def func2(p2):
   print("In func2", p2)

func1(10)

# In func2 10
# In func1 10

# 8
# Define a function that takes two positive integers p1 and p2 as parameters and prints the sum of the two parameters.
# Include code to call the function you have defined.
def sum_two(int1, int2):
    sum = int1 + int2
    print(sum)

sum_two(3, 4)

'''
