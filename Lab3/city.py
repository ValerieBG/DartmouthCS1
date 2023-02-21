# filename: city.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  parse information for a city

from cs1lib import *

RAD = 3


class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        # The city's country code, which is a two-letter string.
        self.country_code = country_code
        # The city's name, which is a string.
        self.name = name
        # The city's region, a two-character string.
        self.region = region
        # The city's population, which is an int.
        self.pop = population
        # The city's latitude, which is a float.
        self.lat = latitude
        # The city's longitude, which is also a float.
        self.long = longitude

    def __str__(self):
        # a string consisting of the city's name, population, latitude, and longitude,
        # separated by commas and with no spaces around the commas.
        return self.name + "," + str(self.pop) + "," + str(self.lat) + "," + str(self.long)

    def draw(self, cx, cy):
        # scale self.lat and self.long to the size of the image,
        # let's say px and py are the scaled values
        if self.lat < 0:
            py = cy + (abs(self.lat)) * 2
        else:
            py = cy - (abs(self.lat)) * 2

        if self.long < 0:
            px = cx - (abs(self.long)) * 2
        else:
            px = cx + (abs(self.long)) * 2

        # call draw_circle(px, py, RAD) to draw that city in its
        # real-life location on the map
        draw_circle(px, py, RAD)