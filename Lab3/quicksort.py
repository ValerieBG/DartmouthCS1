# filename: quicksort.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  recursively sort a list utilizing a comparison function

# function to partition a list by placing and returns an index of a pivot
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]
    while j < r:
        if compare_func(the_list[j], pivot):  # checks if the_list[j] > pivot
            i += 1
            (the_list[i], the_list[j]) = (the_list[j], the_list[i])
            j += 1
        else:  # if the_list[j] <= pivot
            j += 1
    (the_list[r], the_list[i + 1]) = (the_list[i + 1], the_list[r])
    return i + 1  # index where the pivot is


# recursively sort a section of a list utilizing partitioning
def quicksort(the_list, p, r, compare_func):
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, q+1, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)


# sort a whole list using quick sort
def sort(the_list, compare_func):
    p = 0
    r = len(the_list) - 1
    quicksort(the_list, p, r, compare_func)


#######################################
# testing the key quicksort functions #
#######################################
def compare_int_dec(x, y):
    return x >= y


def compare_int_inc(x, y):
    return x <= y


tlist1 = [9, 1, 2, 8, 3, 6, 5, 4, 7]
tlist2 = [1, 4, 24, 5, 6, 3, 8, 2, 9]
tlist3 = [30, 20, 40, 60, 50, 70, 10, 90]

sort(tlist1, compare_int_dec)
sort(tlist2, compare_int_dec)
sort(tlist3, compare_int_inc)

print(tlist1, tlist2, tlist3)
