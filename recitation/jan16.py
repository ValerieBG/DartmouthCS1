# filename: jan16.py
# author:   Valerie Gadapati
# date:     Jan 16, 2023
# purpose:  to draw a bullseye

from cs1lib import *
def bullseye():
    # set background color
    set_fill_color(1,1,1,1) # set background white
    clear()

    # draw outermost circle
    set_fill_color(0, 0, 1, 1) # set blue
    draw_circle(200,200,150)

    # draw middle circle
    set_fill_color(0, 1, 0, 1) # set green
    draw_circle(200, 200, 100)

    # draw inner circle
    set_fill_color(1, 0, 0, 1)
    draw_circle(200, 200, 50)

start_graphics(bullseye)