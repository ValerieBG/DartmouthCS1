## DOCUMENTATION

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        # The city's country code, which is a two-letter string.
        self.country_code = country_code
        # The city's name, which is a string.
        self.name = name
        # The city's region, a two-character string.
        self.region = region
        # The city's population, which is an int.
        self.population = population
        # The city's latitude, which is a float.
        self.latitude = latitude
        # The city's longitude, which is also a float.
        self.longitude = longitude

    def __str__(self):
        # a string consisting of the city's name, population, latitude, and longitude,
        # separated by commas and with no spaces around the commas.
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
