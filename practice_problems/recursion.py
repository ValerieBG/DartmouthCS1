# prac probs for lecture 18, 19, 20 and 22

# 1. What does this code print?
def func1(glist, key, i = 0):
   if i == len(glist):
       return None

   if key == glist[i]:
       return i
   else:
       return func1(glist, key, i + 1)

print(func1([32, 34, 2, 9, 10, -20], 2))
print(func1([32, 34, 2, 9, 10, -20], -2))

# 2. What does this code print?
def func2(glist, i = 0):
   if i == len(glist):
       return False

   if glist[i] % 2 == 0:
       return True

   return func2(glist, i + 1)

print(func2([33, 6, 17, 9, 21]))
print(func2([33, 61, 17, 9, 21]))

# 3. What does this code print?
def func3(x):
   print(x)
   if x == 0 or x == 1:
       return x

   m = func3(x - 2)
   n = func3(x - 1)
   return m + n
func3(4)


# 4. What does this code print?
def func4(x, n):
   if n == 1:
       return x

   p = func4(x, n//2)

   if n % 2 == 0:
       return p*p
   else:
       return p*p*x

print(func4(2, 5))

# 5. The following code was supposed to return the index of the first occurrence of letter “a” in the given string. But there is a mistake in the code. Can you correct it?

def func5(s, i = 0):
   if len(s) == 0:
       return None

   if s[i] == "a":
       return i

   return func5(s, i+1)

print(func6("tester"))

# 1. Define a recursive function that takes a list of integers as a parameter and returns True if the list is sorted in increasing order; otherwise it returns False.
#
# 2. Define a recursive function that takes two strings s1 and s2 as parameters and checks if s2 is a prefix of s1. For example: s2 = “test” and s = “testing” then s1 is a prefix of s2.
#
# 3. Define a recursive function that takes two strings s1 and s2 as parameters and checks if s2 is a substring of s1.
#
# 4. Write a recursive function that takes two non-negative integers n and k as parameters and prints the first k even numbers greater than n.
#
# 5. Write a recursive function that takes two non-negative integers n and k as parameters and returns a list containing first k even numbers greater than n.
#
# 6. Write a recursive function that takes a list of integers glist that is sorted in increasing order and an integer key as a parameter. The function should insert the key into glist such that glist remains sorted.
#
# 7. Write a recursive function find_min that takes a list of integers as a parameter and returns the minimum element in the list.
#
# 8. Write a recursive function find_min_index that takes a list of integers as a parameter and returns that index of the minimum element in the list.
#
# 9. Define a recursive function that takes two positive integers n and k as parameters and does the following:
# prints first k even numbers between 1 and n if there are at least k even numbers between 1 and n
# otherwise it prints all the even numbers between 1 and n.
