# filename: body.py
# author:   Valerie Gadapati
# date:     Feb 20, 2023
# purpose:  create a body class for a celestial body

from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # update the x and y position of the body using the velocity and timestep
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    # update the x and y velocity of the body using the acceleration and timestep
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    # draw a circle to represent the body, scaling meters to pixels
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x * pixels_per_meter + cx, self.y * pixels_per_meter + cy, self.pixel_radius)
