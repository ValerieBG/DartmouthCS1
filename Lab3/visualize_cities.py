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
FRAME_RATE = 4

CX = WINDOW_X // 2
CY = WINDOW_Y // 2

curr_frame = 0
max_frames = 50


def place_map():
    clear()

    img = load_image("world.png")
    draw_image(img, 0, 0)


def map_visual():
    global curr_frame, max_frames
    place_map()

    disable_stroke()
    for i in range(curr_frame):
        set_fill_color(random(), random(), random(), 1)
        world_cities[i].draw(CX, CY)

    if curr_frame < max_frames:
        curr_frame += 1


start_graphics(map_visual, width=WINDOW_X, height=WINDOW_Y, framerate=FRAME_RATE)
