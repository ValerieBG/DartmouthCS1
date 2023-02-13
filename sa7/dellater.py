my_list = [1, 2,3,4,5, 6, 7]
right = 2
left = 6

midpoint = (right + left) // 2
print(my_list[right:left])
print(my_list[midpoint])
print(my_list[left:midpoint])
print(my_list[midpoint:right])
print(midpoint + left)