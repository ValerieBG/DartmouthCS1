# Write the Python code that reads in the city information, sorts it according to the three criteria, and writes out the results to the three files (cities_alpha.txt, cities_population.txt, and cities_latitude.txt), along with all of your comparison functions, in a single file named sort_cities.py.

def partition(the_list, p, r, compare_func):
    # it should return an index q into the list, which is where it places the item chosen as the pivot
    return q