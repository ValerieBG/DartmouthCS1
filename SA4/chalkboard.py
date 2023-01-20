# filename: chalkboard.py
# author:   Valerie Gadapati
# date:     Jan 20, 2023
# purpose:  to open up a graphics window, and allow the user to use the mouse to draw on a simulated chalkboard

from cs1lib import *

# set background color of board to black
def reset_board():
    global default

    set_clear_color(0, 0, 0, 1)
    set_stroke_width(2)

    if default:
        clear()
        white_pen()
        default = False

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

def press(mx, my):
    global draw, old_x, old_y
    old_x = mx
    old_y = my
    draw = True

def release(mx, my):
    global draw
    draw = False

def move(mx, my):
    global curr_x, curr_y
    curr_x = mx
    curr_y = my

def graphics():
    global draw, old_x, old_y, curr_x, curr_y
    reset_board()

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

start_graphics(graphics, 2400, mouse_press=press, mouse_release=release, mouse_move=move, key_press=keypress)
