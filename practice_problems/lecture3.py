
# mark the order the lines are executed
def func1(): # 1, 5
    print("In func1") # 6

print("first pp")# 2
print("practice program counter") #3
func1() #4
print("done") #7


# Define a function named my_message that prints at least three lines of message of your choice.
def my_message(): # 1, 3, 8
    print("line 1") #4, 9
    print("line 2") #5, 10
    print("line 3")#6, 11

# Call the function twice.
my_message() #2
my_message() #7
# Mark the order in which the statements (lines of code) are executed in your program.


# mark the order the lines are executed
def func1(): #1, 5
    print("In func1") #6

def func2(): #2, 9
    print("In func2") #10

print("multi function") #3
func1() #4
print("done with 1") #7
func2() #8
print("done") #11