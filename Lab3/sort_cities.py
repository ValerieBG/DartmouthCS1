## need documentation

from city import City
from quicksort import *


def compare_population(city1, city2):
    return city1.pop >= city2.pop


def compare_alphabet(city1, city2):
    x = city1.name.lower
    y = city2.name.lower
    return x <= y


def compare_latitude(city1, city2):
    return city1.lat <= city2.lat


### testing shit
tlist = [9, 1, 2, 8, 3, 6, 5, 4, 7]

def compare_int(x, y):
    return x >= y

sort(tlist, compare_int)
print(tlist)


###



cities_list = []

# open the provided text file
world_data = open("world_cities.txt", "r")


for line in world_data:
    # for each line of the file, strip it and split it by commas, returning a list of the info
    line = line.strip()
    line = line.split(",")
    # use the given list to create a city object from the line, converting as needed
    place = City(line[0], line[1], line[2], int(line[3]), float(line[4]), float(line[5]))
    # add the new city object to the list
    cities_list.append(place)

cities_population = open("cities_population.txt", "w")

sort(cities_list, compare_population)
for city in cities_list:
    cities_population.write(str(city) + "\n")

# close the given data file
world_data.close()
cities_population.close()
