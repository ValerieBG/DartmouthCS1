def func1():
   func2() # because of this not being defined
   print("In func1")

func1() # would cause error
def func2():
   print("In func2")

func2()
