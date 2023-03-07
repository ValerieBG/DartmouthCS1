# filename: map_plot.py
# author:   Valerie Gadapati
# date:     Mar 7, 2023
# purpose:  to visualize an interactive map to plot paths

from cs1lib import *
from load_graph import load_graph
from bfs import *

WINDOW_X = 1012
WINDOW_Y = 811


def load_map():
    global start

    if start:
        # draw the map as the background
        clear()

        img = load_image("dartmouth_map.png")
        draw_image(img, 0, 0)
        # print("map drawn") # for testing (map drawing should only run once)

        # only run once on startup
        start = False


# function to check mouse being pressed
def press(mx, my):
    global select, start_x, start_y
    start_x = mx
    start_y = my
    select = True


# function to check mouse being moved
def move(mx, my):
    global goal_x, goal_y
    goal_x = mx
    goal_y = my


# main visualization function
def visualize():
    global select, goal_x, goal_y, start_vert, goal_vert, start_x, start_y

    load_map()

    # draw all nodes and edges
    for n in vert_dict:
        vert_dict[n].draw_all_adj(0, 0.4, 0.25)
        vert_dict[n].draw_node(0, 0.4, 0.25)

    goal_vert = None
    # check to find start and goal vertices
    for elem in vert_dict:
        if select and vert_dict[elem].in_node(start_x, start_y):
            start_vert = vert_dict[elem]
            vert_dict[elem].draw_node(1, 0, 0)
        if vert_dict[elem].in_node(goal_x, goal_y):
            vert_dict[elem].draw_node(1, 0, 0)
            goal_vert = vert_dict[elem]

    # once there is an identified start and end visualize the path
    if start_vert is not None and goal_vert is not None:
        path = breadth_first_search(start_vert, goal_vert)
        for i in range(len(path) - 1):
            path[i].draw_edge(path[i+1], 1, 0, 0)


# global variables
start = True
start_x = 0
start_y = 0
goal_x = 0
goal_y = 0
start_vert = None
goal_vert = None
select = False

# create vertex dictionary
vert_dict = load_graph("dartmouth_graph.txt")

start_graphics(visualize, width=WINDOW_X, height=WINDOW_Y, mouse_press=press, mouse_move=move)
