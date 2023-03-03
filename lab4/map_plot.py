# DOCU HERE

from cs1lib import *

WINDOW_X = 1012
WINDOW_Y = 811


def load_map():
    global start
    if start:
        clear()

        img = load_image("dartmouth_map.png")
        draw_image(img, 0, 0)

        # only run once on startup
        start = False


def visualize():
    load_map()

start = True

start_graphics(visualize, width=WINDOW_X, height=WINDOW_Y)


# Allow the user to select a starting vertex for the search. As the user moves the mouse around after pressing and
# releasing the mouse button on a starting vertex, if the mouse is on another vertex and the button is not pressed,
# use this other vertex as the goal. You can call the mouse location as “on” another vertex if it’s within the smallest
# square that surrounds the vertex. In other words, the mouse doesn’t have to be in the circle for the vertex, but just
# in the smallest surrounding square; that makes the test for inclusion really simple. (Hint: Write a method in the
# Vertex class that takes as parameters x- and y-coordinates and returns a boolean indicating whether this location is
# within the smallest surrounding square for this vertex.)
#
# The best way I can think of doing this is, each time through your main graphics loop, check every vertex in the
# dictionary to see whether the mouse is on it. If you need to, you can store references to the start vertex and the
# goal vertex in global variables. (I didn’t need globals for them, however.) For debugging purposes, draw these two
# vertices in red so that you can easily see them.
#
# Fully test and debug displaying the graph and selecting the start and goal vertices before moving on.
