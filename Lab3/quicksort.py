## DOUCEMTATOIN UP EHRE

# Write the Python code that reads in the city information, sorts it according to the three criteria, and writes out the results to the three files (cities_alpha.txt, cities_population.txt, and cities_latitude.txt), along with all of your comparison functions, in a single file named quicksort.py.

def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]
    while j < r:
        if compare_func(the_list[j], pivot):  # checks if the_list[j] > pivot
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
            j += 1
        else:  # if the_list[j] <= pivot
            j += 1
    the_list[r], the_list[i + 1] = the_list[i + 1], the_list[r]
    return i + 1  # index where the pivot is


def quicksort(the_list, p, r, compare_func):
    if r <= p:
        return None
    q = partition(the_list, p, r, compare_func)
    partition(the_list, q+1, r, compare_func)
    partition(the_list, p, q-1, compare_func)

def sort(the_list, compare_func):
    p = 0
    r = len(the_list) - 1
    quicksort(the_list, p, r, compare_func)

