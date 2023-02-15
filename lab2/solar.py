# filename: solar.py
# author:   Valerie Gadapati
# date:     Feb 20, 2023
# purpose:  to simulate our solar system's first 4 planets moving around the sun
# NOTE:     I spoke w Daniel Chen about interpreting the Nasa chart and appropriate conversions/units

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # real seconds per simulation second
PIXELS_PER_METER = 1 / 1.5e9  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_sys.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_sys.update(TIMESTEP * TIME_SCALE)


# source: https://nssdc.gsfc.nasa.gov/planetary/factsheet/, converted units as needed
# sun has no velocity because it is the center of the system
sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
# the first four planets
mercury = Body(0.330e24, 0, 57.9e9, 47400, 0, 3, 0.75, 0.75, 0.75)
venus = Body(4.87e24, 0, 108.2e9, 35000, 0, 5, 240/255, 230/255, 140/255)
earth = Body(5.9736e24, 0, 149.6e9, 29800, 0, 5, 0, 0, 1)
mars = Body(0.642e24, 0, 228.0e9, 24100, 0, 10, 193/255, 68/255, 14/255)

solar_sys = System([sun, mercury, venus, earth, mars])

start_graphics(main, 2400, framerate=FRAMERATE)
