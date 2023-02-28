# filename: visualize_cities.py
# author:   Valerie Gadapati
# date:     Mar 1, 2023
# purpose:  display cities given coordinates on a world map image

from cs1lib import *
from random import *

# constants about the window size
WINDOW_X = 720
WINDOW_Y = 360
FRAME_RATE = 4

# center of the image
CX = WINDOW_X // 2
CY = WINDOW_Y // 2


# function to load and draw the map background
def place_map():
    clear()

    img = load_image("world.png")
    draw_image(img, 0, 0)


# main drawing function
def map_visual():
    global curr_frame, max_frames, pop_cities_list
    place_map()

    for i in range(curr_frame):
        # randomly color the insides of the dots
        set_fill_color(random(), random(), random(), 1)

        x = 2 * pop_cities_list[i][3]
        y = 2 * pop_cities_list[i][2]
        draw_circle(CX + x, CY - y, 3)

    # with each frame, draw one more city, creating an animation
    if curr_frame < max_frames:
        curr_frame += 1


# variables to animate the visualization
curr_frame = 0
max_frames = 50  # number of cities to draw

# make a list of the top 50 cities from a sorted file
pop_cities_list = []

pop_cities_sorted = open("cities_population.txt", "r")
for line in pop_cities_sorted:
    line = line.strip()
    line = line.split(",")
    pop_cities_list.append([line[0], int(line[1]), float(line[2]), float(line[3])])

pop_cities_sorted.close()

start_graphics(map_visual, width=WINDOW_X, height=WINDOW_Y, framerate=FRAME_RATE)
