# filename: solar.py
# author:   Valerie Gadapati
# date:     Feb 20, 2023
# purpose:  to simulate our solar system's first 4 planets moving around the sun

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # real seconds per simulation second
PIXELS_PER_METER = 1 / 1.5e9  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

# function to check mouse being pressed
def press(mx, my):
    global click, curr_x, curr_y
    curr_x = mx  # the starting position of the line should be when it is pressed
    curr_y = my
    click = True  # if the mouse is pressed, drawing should be occurring

def release(mx, my):
    global click
    # click = False  # when the mouse is released, no more drawing should be occurring

def keypress(key):
    global click

    if key == 'q':
        click = False

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    set_font_size(14)
    enable_stroke()
    set_stroke_color(1, 0, 0, 1)
    draw_text("click a planet to see some fun facts! press q to close fact sheet.", 7, 15)

    # Draw the system in its current state.
    solar_sys.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_sys.update(TIMESTEP * TIME_SCALE)

    if click:
        if (WINDOW_WIDTH//2 + mars.x*PIXELS_PER_METER - mars.pixel_radius) <= curr_x <= (WINDOW_WIDTH//2 + mars.x*PIXELS_PER_METER + mars.pixel_radius):
            mars_fact = load_image("mars.jpg")
            draw_image(mars_fact, 10, 20)

curr_x = 0
curr_y = 0
click = False

# source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/, converted units as needed
# sun has no velocity because it is the center of the system
sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
# the first four planets
mercury = Body(0.330e24, 0, 57.9e9, 47400, 0, 3, 0.75, 0.75, 0.75)
venus = Body(4.87e24, 0, 108.2e9, 35000, 0, 5, 240/255, 230/255, 140/255)
earth = Body(5.9736e24, 0, 149.6e9, 29800, 0, 5, 0, 0, 1)
mars = Body(0.642e24, 0, 228.0e9, 24100, 0, 10, 193/255, 68/255, 14/255)

solar_sys = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE, mouse_press=press, mouse_release=release, key_press=keypress)
