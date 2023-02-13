# filename: system.py
# author:   Valerie Gadapati
# date:     Feb 20, 2023
# purpose:  create a system class to define interactions between celestial bodies
from math import sqrt

# constant used in acceleration calculations
GRAVITY = 6.67384e-11


class System:
    # initialize a system when given a list of bodies (objects of the Body class)
    def __init__(self, list_bodies):
        self.bodies = list_bodies

    # computes the accelerations on each body and then calls methods in Body to update the velocity and position
    # of each body.
    def update(self, timestep):
        # update the position of each body
        for bod in self.bodies:
            bod.update_position(timestep)

        # for each body, compute the acceleration and update the velocity using the new acceleration values
        for i in range(len(self.bodies)):
            (ax, ay) = self.compute_acceleration(i)
            self.bodies[i].update_velocity(ax, ay, timestep)

    # draw each body in the system
    def draw(self, cx, cy, pixels_per_meter):
        for bod in self.bodies:
            bod.draw(cx, cy, pixels_per_meter)

    # compute the acceleration of an object based on gravitational forces around it
    def compute_acceleration(self, n):
        # starts as zero in both directions
        a_x = 0
        a_y = 0

        # identify the given body
        body1 = self.bodies[n]

        for i in range(0, len(self.bodies)):
            if i != n:  # don't calculate hte gravity of itself
                # identify the body you will calculate against
                body2 = self.bodies[i]

                # raw component distances (x2 - x1 and y2 - y1)
                dx = (body2.x - body1.x)
                dy = (body2.y - body1.y)

                # calculate non-linear distance between the objects
                dist = sqrt((dx * dx) + (dy * dy))  # pythagorean theorem

                # calculate the acceleration using (gravity constant * mass1 * mass2) / dist^2
                a = (GRAVITY * body2.mass) / (dist * dist)

                # calculate the x and y components of the acceleration
                a_x_bod = (a * dx) / dist
                a_y_bod = (a * dy) / dist

                # continue adding the calculated components to the total x and y components, for each other body
                a_x += a_x_bod
                a_y += a_y_bod

        return a_x, a_y  # return a tuple with two values, the accelerations in x and y
