# filename: read_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  parse and write to text files given a text file of cities

from city import *

# list to hold the cities post-processing
world_cities = []

# open the provided text file
world_data = open("world_cities.txt", "r")
for line in world_data:
    # for each line of the file, strip it and split it by commas, returning a list of the info
    line = line.strip()
    line = line.split(",")
    # use the given list to create a city object from the line, converting as needed
    place = City(line[0], line[1], line[2], int(line[3]), float(line[4]), float(line[5]))
    # add the new city object to the list
    world_cities.append(place)
# close the given data file
world_data.close()

# write the new city list into its own file
output = open("cities_out.txt", "w")
for i in range(len(world_cities)):
    # if the item is not the last in the list, add a new line
    # str function for city objects adds formatting like commas
    if i != len(world_cities) - 1:
        output.write(str(world_cities[i]) + '\n')
    else:
        output.write(str(world_cities[i]))
# close the file
output.close()
