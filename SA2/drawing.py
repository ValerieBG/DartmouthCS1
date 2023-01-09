# filename: drawing.py
# author:   Valerie Gadapati
# date:     Jan 8, 2023
# purpose:  to draw the cover of the children's book "Don't Let the Pigeon Drive the Bus!"
#           by Mo Willems for Dartmouth CS1 SA2

from cs1lib import *

# functions to set relevant fill colors, rbg values taken from the source material
def set_fill_blue():
    set_fill_color(173/255, 204/255, 192/255, 1)

def set_fill_white():
    set_fill_color(1, 1, 1, 1)

def set_fill_yellow(): #for the beak
    set_fill_color(255/255, 255/255, 51/255, 1)

def set_fill_orange():
    set_fill_color(244/255, 175/255, 107/255, 1)

def set_fill_black():
    set_fill_color(0, 0, 0, 1)

# functions to set relevant stroke colors, rbg values taken from the source material
def set_stroke_black():
    set_stroke_color(0, 0, 0, 1)

def set_stroke_white():
    set_stroke_color(1, 1, 1, 1)

def set_stroke_orange():
    set_stroke_color(244/255, 175/255, 107/255, 1)

def set_stroke_blue():
    set_stroke_color(173/255, 204/255, 192/255, 1)

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

    # draw the body of the speech bubble
    draw_ellipse(ellipse_x, ellipse_y, ellipse_xr, ellipse_yr)

    # finish the speech bubble tail utilizing ellipse for scale
    point_1_x = ellipse_x+(2*ellipse_xr//3)
    point_1_y = ellipse_y+(3*ellipse_yr//4)
    point_2_x = ellipse_x + (ellipse_xr // 4)
    point_2_y = ellipse_y+(7*ellipse_yr//8)
    point_3_x = point_1_x + (point_1_x-point_2_x)//2
    point_3_y = point_2_y + (ellipse_yr//2)

    draw_triangle(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)

def draw_pigeon():
    # set variables about the pigeon to reference in the drawing
    neck_length = 90
    neck_width = 30
    body_x = 320
    body_y = 300
    body_r = 50

    # set more variables for use in pigeon head
    head_x = body_x - body_r + (neck_width // 2)
    head_y = body_y - neck_length
    head_r = 30

    # draw left leg
    set_stroke_black()
    draw_line(body_x-(body_r//3), body_y-(3*body_r//4), body_x-(body_r//3), body_y+(5*body_r//3))
    draw_line(body_x-(body_r//3), body_y+(4*body_r//3), body_x-(body_r//2), body_y+(5*body_r//3))
    draw_line(body_x-(body_r//3), body_y+(4*body_r//3), body_x-(body_r//2)+(3*body_r//8), body_y+(5*body_r//3))

    # draw right leg
    draw_line(body_x + (body_r // 3), body_y - (3 * body_r // 4), body_x + (body_r // 3), body_y + (5 * body_r // 3))
    draw_line(body_x + (body_r // 3), body_y + (4 * body_r // 3), body_x + (body_r // 2), body_y + (5 * body_r // 3))
    draw_line(body_x + (body_r // 3), body_y + (4 * body_r // 3), body_x - (body_r // 2) + (5 * body_r // 8), body_y + (5 * body_r // 3))

    # draw the body
    set_fill_blue()
    set_stroke_black()
    draw_circle(body_x, body_y, body_r)

    # refine body
    set_fill_orange()
    set_stroke_orange()
    draw_rectangle(body_x-body_r, body_y-body_r, body_r*2, body_r)  # create the semi circle
    set_stroke_black()
    draw_line(body_x-(body_r-neck_width), body_y, body_x+body_r, body_y)  # redraw the line to maintain bird border

    # draw neck
    set_stroke_black()
    set_fill_blue()
    draw_rectangle(body_x-body_r, body_y-neck_length, neck_width, neck_length)

    # refine neck
    set_stroke_blue()
    set_fill_blue()
    draw_circle(body_x - body_r + (neck_width//2), body_y, neck_width//2)  # cover bottom edge to maintain bird border

    # draw band on neck
    set_stroke_black()
    set_fill_white()
    draw_rectangle(body_x-body_r, body_y-(neck_length//2), neck_width, (neck_length//5))

    # draw pigeon beak
    set_fill_yellow()
    set_stroke_black()
    draw_triangle(head_x-head_r-(head_r//3), head_y, head_x-head_r, head_y, head_x-head_r+(head_r//3), head_y-(head_r//3))
    draw_triangle(head_x-head_r-(head_r//6), head_y, head_x-head_r, head_y, head_x-head_r+(head_r//3), head_y+(head_r//3))

    # draw pigeon head
    set_stroke_black()
    set_fill_blue()
    draw_circle(head_x, head_y, head_r)

    # draw pigeon eye
    set_fill_white()
    set_stroke_black()
    draw_circle(head_x, head_y, head_r//2)  # the white of the eye
    set_fill_black()
    draw_circle(head_x+(head_r//4), head_y, head_r//4)  # the pupil of the eye

def write_name():
    name = "Valerie Gadapati"
    set_stroke_black() # set text color to black
    set_font("PT Serif")
    set_font_size(20)
    draw_text(name, 30, 370)

def draw_cover():
    set_background_orange()
    draw_speech_bubble()
    draw_pigeon()
    write_name()

start_graphics(draw_cover)