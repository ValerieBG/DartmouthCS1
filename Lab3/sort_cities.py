# filename: sort_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  sort cities by certain characteristics

from city import City
from quicksort import *


# function to compare if city1 has a greater population than city2
def compare_population(city1, city2):
    return city1.pop >= city2.pop


# function to compare if city1 alphabetically comes before city2
def compare_alphabet(city1, city2):
    x = city1.name.lower()
    y = city2.name.lower()
    return x <= y


# function to compare if city1 has a smaller latitude than city2
def compare_latitude(city1, city2):
    return city1.lat <= city2.lat


# create a list of the cities given in a file
cities_list = []

world_data = open("world_cities.txt", "r")

for line in world_data:
    line = line.strip()
    line = line.split(",")
    place = City(line[0], line[1], line[2], int(line[3]), float(line[4]), float(line[5]))
    cities_list.append(place)

# sort by population and write to a file
cities_population = open("cities_population.txt", "w")
sort(cities_list, compare_population)
for city in cities_list:
    cities_population.write(str(city) + "\n")

# sort alphabetically and write to a file
cities_alpha = open("cities_alpha.txt", "w")
sort(cities_list, compare_alphabet)
for city in cities_list:
    cities_alpha.write(str(city) + "\n")

# sort by latitude and write to a file
cities_lat = open("cities_latitude.txt", "w")
sort(cities_list, compare_latitude)
for city in cities_list:
    cities_lat.write(str(city) + "\n")

# close all files after use
world_data.close()
cities_population.close()
cities_alpha.close()
cities_lat.close()
