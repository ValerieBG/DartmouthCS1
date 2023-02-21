# filename: visualize_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  display cities given coordinates on a world map image

from city import *
from cs1lib import *
from read_cities import world_cities
from random import *

WINDOW_X = 720
WINDOW_Y = 360

CX = WINDOW_X // 2
CY = WINDOW_Y // 2

def place_map():
    clear()

    img = load_image("world.png")
    draw_image(img, 0, 0)


def place_dots():
    disable_stroke()
    for i in range(0, 50):
        set_fill_color(random(), random(), random(), 1)
        world_cities[i].draw(CX, CY)


def map_visual():
    place_map()
    place_dots()


start_graphics(map_visual, width=WINDOW_X, height=WINDOW_Y, framerate=5)
