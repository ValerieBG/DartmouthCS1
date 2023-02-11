# filename: system.py
# author:   Valerie Gadapati
# date:     Feb XX, 2023
# purpose:  XX
from math import sqrt

GRAVITY = 6.67384e-11


class System:
    def __init__(self, list_bodies):
        self.bodies = list_bodies

    # computes the accelerations on each body and then calls methods in Body to update the velocity and position
    # of each body.
    def update(self, timestep):
        for bod in self.bodies:
            bod.update_position(timestep)

        i = 0
        while i < len(self.bodies):
            (ax, ay) = self.compute_acceleration(i)
            self.bodies[i].update_velocity(ax, ay, timestep)
            i = i + 1

    def draw(self, cx, cy, pixels_per_meter):
        for bod in self.bodies:
            bod.draw(cx, cy, pixels_per_meter)

    def compute_acceleration(self, n):
        a_x = 0
        a_y = 0

        body1 = self.bodies[n]

        i = 0
        while i < n:
            body2 = self.bodies[i]
            dx = (body2.x - body1.x)
            dy = (body2.y - body1.y)

            dist = sqrt((dx * dx) + (dy * dy))  # pythagorean theorem
            a = (GRAVITY * body2.mass) / (dist * dist)

            a_x_bod = (a * dx) / dist
            a_y_bod = (a * dy) / dist
            a_x += a_x_bod
            a_y += a_y_bod

            i = i + 1

        return a_x, a_y  # return a tuple with two values, the accelerations in x and y


