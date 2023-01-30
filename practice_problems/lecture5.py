# Without running the programs, find out what each of the following programs will print?

'''
# 1
n = 5
if n % 5 == 0:
   print("five")
else:
   print("non-five")

# five

# 2
n = 7
if n % 5 == 0:
   print("five")
else:
   print("non-five")

# non-five

# 3
n1 = 10
n2 = 20
n3 = 10

if n1 == n2: # false
   print("yes")
elif n2 == n3: # false
   print("yes")
elif n3 == n1: # true!
   print("yes")
else:
   print("no")

# yes

# 4
n1 = 10
n2 = 10
n3 = 10

if n1 == n2: # true!
   print("yes")
elif n2 == n3: # will not evaluate elifs
   print("yes")
elif n3 == n1:
   print("yes")
else:
   print("no")

# yes

# 5
n1 = 10
n2 = 10
n3 = 20

if n1 == n2: #true
   print("yes")
if n2 == n3: # false
   print("yes")
if n3 == n1: # false
   print("yes")
else: # connected to the most recent if... will run!
   print("no")

# yes
# no

# 6
n1 = 10
n2 = 10
n3 = 10

if n1 == n2: # true
   print("yes")
if n2 == n3: # true
   print("yes")
if n3 == n1: # true
   print("yes")
else:
   print("no")

# yes
# yes
# yes

# 7
a1 = 60
a2 = 60
a3 = 60

if (a1 + a2 + a3) != 180:
   print("Not a triangle")
else:
    if a1 == a2 and a2 == a3:
        print("Equilateral")
    elif (a1 == a2) or (a2 == a3) or (a1 == a3):  # change this from if to elif
        print("Isosceles")
    else:
        print("Scalene")

'''
