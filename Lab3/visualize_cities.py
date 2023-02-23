# filename: visualize_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  display cities given coordinates on a world map image

from cs1lib import *
from read_cities import world_cities
from random import *

# constants about the window size
WINDOW_X = 720
WINDOW_Y = 360
FRAME_RATE = 4

# center of the image
CX = WINDOW_X // 2
CY = WINDOW_Y // 2

# variables to animate the visualization
curr_frame = 0
max_frames = 50  # number of cities to draw


# function to load and draw the map background
def place_map():
    clear()

    img = load_image("world.png")
    draw_image(img, 0, 0)


# main drawing function
def map_visual():
    global curr_frame, max_frames
    place_map()

    for i in range(curr_frame):
        # randomly color the insides of the dots
        set_fill_color(random(), random(), random(), 1)
        # draw each city
        world_cities[i].draw(CX, CY)

    # with each frame, draw one more city, creating an animation
    if curr_frame < max_frames:
        curr_frame += 1


start_graphics(map_visual, width=WINDOW_X, height=WINDOW_Y, framerate=FRAME_RATE)
