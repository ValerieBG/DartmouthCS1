# filename: chalkboard.py
# author:   Valerie Gadapati
# date:     Jan 22, 2023
# purpose:  use a graphics window to allow the user to draw on a simulated chalkboard with their mouse and keyboard

from cs1lib import *

# set default state for the board: black background, white pen and set stroke width
def reset_board():
    global default  # global variable to make sure the canvas doesn't constantly loop and clear states

    set_clear_color(0, 0, 0, 1)  # set background black
    set_stroke_width(2)

    if default:
        clear()
        white_pen()
        default = False  # change state to false, so it only runs once in the beginning


# change line color to white
def white_pen():
    set_stroke_color(1, 1, 1, 1)

# change line color to red
def red_pen():
    set_stroke_color(1, 0, 0, 1)

# change line color to blue
def blue_pen():
    set_stroke_color(0, 0, 1, 1)

# change line color to green
def green_pen():
    set_stroke_color(0, 1, 0, 1)

# change line color to yellow
def yellow_pen():
    set_stroke_color(1, 1, 0, 1)


# function to check mouse being pressed
def press(mx, my):
    global draw, old_x, old_y
    old_x = mx  # the starting position of the line should be when it is pressed
    old_y = my
    draw = True  # if the mouse is pressed, drawing should be occurring

def release(mx, my):
    global draw
    draw = False  # when the mouse is released, no more drawing should be occurring


def move(mx, my):
    global curr_x, curr_y
    curr_x = mx  # as the mouse moves, set its new value to be used to draw a line
    curr_y = my


# function to change the color of the pen based on keyboard input
def keypress(key):
    if key == 'r':
        red_pen()
    elif key == 'b':
        blue_pen()
    elif key == 'g':
        green_pen()
    elif key == 'y':
        yellow_pen()
    elif key == 'w':
        white_pen()


def graphics():
    global draw, old_x, old_y, curr_x, curr_y
    reset_board()  # initialize the board to its default state

    if draw:
        draw_line(old_x, old_y, curr_x, curr_y)
        # update old x and y to the end point of the most recent line
        old_x = curr_x
        old_y = curr_y


# state variables
old_x = 0
old_y = 0
curr_x = 0
curr_y = 0
draw = False
default = True

# utilize callback functions to check mouse position/status and keyboard inputs to draw
start_graphics(graphics, 2400, mouse_press=press, mouse_release=release, mouse_move=move, key_press=keypress)
