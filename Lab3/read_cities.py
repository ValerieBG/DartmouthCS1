# filename: read_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  parse and write to text files given a text file of cities

from city import *

# Although each line of world_cities.txt begins with a non-whitespace character, each line ends with a newline, and
# newline is a whitespace character. Therefore, you will want to call strip on each line of the file and then call
# split to separate the information by the commas.
world_cities = []
world_data = open("world_cities.txt", "r")
for line in world_data:
    line = line.strip()
    line = line.split(",")
    # Once you have a list of information in a particular line of the file, you can send that information into the City
    # constructor. Since split gives you a list, you can just index into that list for each item. Remember that some of the
    # instance variables in a City object are not strings, and so you will have to convert these strings to the appropriate
    # types.
    place = City(line[0], line[1], line[2], int(line[3]), float(line[4]), float(line[5]))
    # The City constructor will give you back, as you undoubtedly know, a reference to a City object. You should append that
    # reference to a list that you're building up. When you're done, the list should comprise 47913 references to City
    # objects, one for each line in world_cities.txt.
    world_cities.append(place)

world_data.close()

# write one line to it for each City object. The line for each city should contain the string returned by calling str
# on the corresponding City object. Because the __str__ method inserts commas, cities_out.txt will be a CSV file. You'll
# need to add the newline for each city. When you're done, your cities_out.txt file should have 47913 lines.
output = open("cities_out.txt", "w")
for i in range(len(world_cities)):
    if i != len(world_cities) - 1:
        output.write(str(world_cities[i]) + '\n')
    else:
        output.write(str(world_cities[i]))

output.close()
