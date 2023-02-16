my_list = [100, 406, 482, 497, 534, 627, 867, 965, 968]
left = 2
right = len(my_list) - 1

midpoint = (right + left) // 2
print("midpoint is index ", midpoint, "  ;  value is ", my_list[midpoint])
print(my_list[left:midpoint])
print(my_list[midpoint + 1: right + 1])
print(int((right+left)/2) == (right + left) // 2)



# starting at index left and going up to and including the index just before midpoint
# left, midpoint-1
# starting at the index just after midpoint and going up to and including index right
# midpoint+1, right