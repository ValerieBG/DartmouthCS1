# filename: pigeonCover.py
# author:   Valerie Gadapati
# date:     []
# purpose: to draw the cover of the children's book "Don't Let the Pigeon Drive the Bus!"
# by Mo Willems for Dartmouth CS1 SA2

from cs1lib import *

# functions to set relevant fill colors, rbg values taken from the source material
def set_fill_blue():
    set_fill_color(173/255, 204/255, 192/255, 1)

def set_fill_white():
    set_fill_color(1, 1, 1, 1)

def set_fill_yellow(): #for the beak
    set_fill_color(251/255, 200/255, 58/255, 1)

# functions to set relevant stroke colors, rbg values taken from the source material
def set_stroke_black():
    set_stroke_color(0, 0, 0, 1)

def set_stroke_white():
    set_stroke_color(1, 1, 1, 1)

# function to set the background color of the cover, rbg values taken from the source material
def set_background_orange():
    set_clear_color(244/255, 175/255, 107/255, 1)
    clear()

# function to draw the speech bubble, including the text of the title of the book
def draw_speech_bubble():
    # draw the circular part of the speech bubble
    set_fill_white()
    set_stroke_white()

    # set variables for ellipse
    ellipse_x = 100
    ellipse_y = 120
    ellipse_xr = 150
    ellipse_yr = 180
    draw_ellipse(ellipse_x, ellipse_y, ellipse_xr, ellipse_yr)

    # finish the speech bubble tail
    draw_triangle(ellipse_x+ellipse_xr, ellipse_y+ellipse_yr, ellipse_x+(ellipse_xr/2), ellipse_y+(ellipse_yr/2), 250,
                  250)

    # add formatted text to the speech bubble, if desired
    title = ""  # "Don't Let the Pigeon Drive the Bus!"
    set_stroke_color(0, 0, 0, 1)  # set text color to black
    set_font("PT Serif")
    set_font_size(40)
    draw_text(title, 50, 50)

def draw():
    set_background_orange()
    #draw_pigeon()
    draw_speech_bubble()

start_graphics(draw)