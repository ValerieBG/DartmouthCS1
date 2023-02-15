# filename: solar.py
# author:   Valerie Gadapati
# date:     Feb 20, 2023
# purpose:  to simulate our solar system's first 4 planets moving around the sun
# EXTRA CREDIT: when you click on a planet, randomly display 1 of 3 possible fun facts about the planet!
#               utilizes image and text generation from cs1lib, the random lib, and Canva for some graphics


from cs1lib import *
from system import System
from body import Body
from random import randint

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # real seconds per simulation second
PIXELS_PER_METER = 1 / 1.5e9  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


# function to check mouse being pressed
def press(mx, my):
    global click, curr_x, curr_y, fact_num
    curr_x = mx
    curr_y = my
    click = True
    fact_num = randint(1, 3)


# function to check keyboard key being pressed
def keypress(key):
    global click

    if key == 'q':
        click = False


# use a random number to choose between 3 facts to display
def choose_fact():
    global fact_num

    return str(fact_num)

def main():
    global fact_num

    set_clear_color(0, 0, 0)    # black background

    clear()

    set_font_size(14)
    enable_stroke()
    set_stroke_color(1, 0, 0, 1)
    draw_text("click a planet to see some fun facts! press q to close fact sheet.", 7, 15)

    # if no planet is clicked, continue the movement of the planets
    if not click:
        # Draw the system in its current state.
        solar_sys.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

        # Update the system for its next state.
        solar_sys.update(TIMESTEP * TIME_SCALE)
    # once a planet is clicked, pause the movement and check which planet
    else:
        # mars click
        if (WINDOW_WIDTH//2 + mars.x*PIXELS_PER_METER - mars.pixel_radius) <= curr_x <= (
                WINDOW_WIDTH//2 + mars.x*PIXELS_PER_METER + mars.pixel_radius) and (
                WINDOW_WIDTH//2 + mars.y * PIXELS_PER_METER - mars.pixel_radius) <= curr_y <= (
                WINDOW_WIDTH//2 + mars.y * PIXELS_PER_METER + mars.pixel_radius):
            # mars facts via mars.nasa.gov
            mars_fact = load_image("mars_pics/mars" + choose_fact() + ".jpg")
            draw_image(mars_fact, 20, 50)
        # mercury click
        if (WINDOW_WIDTH // 2 + mercury.x * PIXELS_PER_METER - mercury.pixel_radius) <= curr_x <= (
                WINDOW_WIDTH // 2 + mercury.x * PIXELS_PER_METER + mercury.pixel_radius) and (
                WINDOW_WIDTH // 2 + mercury.y * PIXELS_PER_METER - mercury.pixel_radius) <= curr_y <= (
                WINDOW_WIDTH // 2 + mercury.y * PIXELS_PER_METER + mercury.pixel_radius):
            # mercury pics made by me in canva, appropriate credit given
            mercury_fact = load_image("mercury_pics/mercury" + choose_fact() + ".jpg")
            draw_image(mercury_fact, 20, 50)
        # venus click
        if (WINDOW_WIDTH // 2 + venus.x * PIXELS_PER_METER - venus.pixel_radius) <= curr_x <= (
                WINDOW_WIDTH // 2 + venus.x * PIXELS_PER_METER + venus.pixel_radius) and (
                WINDOW_WIDTH // 2 + venus.y * PIXELS_PER_METER - venus.pixel_radius) <= curr_y <= (
                WINDOW_WIDTH // 2 + venus.y * PIXELS_PER_METER + venus.pixel_radius):
            # venus pics made by me in canva, appropriate credit given
            venus_fact = load_image("venus_pics/venus" + choose_fact() + ".jpg")
            draw_image(venus_fact, 20, 50)
        # earth click
        if (WINDOW_WIDTH // 2 + earth.x * PIXELS_PER_METER - earth.pixel_radius) <= curr_x <= (
                WINDOW_WIDTH // 2 + earth.x * PIXELS_PER_METER + earth.pixel_radius) and (
                WINDOW_WIDTH // 2 + earth.y * PIXELS_PER_METER - earth.pixel_radius) <= curr_y <= (
                WINDOW_WIDTH // 2 + earth.y * PIXELS_PER_METER + earth.pixel_radius):
            # earth pics made by me in canva, appropriate credit given
            earth_fact = load_image("earth_pics/earth" + choose_fact() + ".jpg")
            draw_image(earth_fact, 20, 50)


curr_x = 0
curr_y = 0
click = False
fact_num = 0

# source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/, converted units as needed
# sun has no velocity because it is the center of the system
sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
# the first four planets
mercury = Body(0.330e24, 0, 57.9e9, 47400, 0, 3, 0.75, 0.75, 0.75)
venus = Body(4.87e24, 0, 108.2e9, 35000, 0, 5, 240/255, 230/255, 140/255)
earth = Body(5.9736e24, 0, 149.6e9, 29800, 0, 5, 0, 0, 1)
mars = Body(0.642e24, 0, 228.0e9, 24100, 0, 10, 193/255, 68/255, 14/255)

solar_sys = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE, mouse_press=press, key_press=keypress)
