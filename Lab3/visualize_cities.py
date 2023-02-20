# filename: visualize_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  display cities given coordinates on a world map image

from city import *
from cs1lib import *

WINDOW_Y = 500
WINDOW_X = 700


def place_map():
    clear()

    img = load_image("world.png")
    draw_image(img, 0, 0)


def draw(self, cx, cy):
    # scale self.lat and self.long to the size of the image,

    # let's say px and py are the scaled values

    # call draw_circle(px, py, RAD) to draw that city in its
    # real-life location on the map


start_graphics(place_map, width=720, height=360)
