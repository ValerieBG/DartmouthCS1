# filename: system.py
# author:   Valerie Gadapati
# date:     Feb XX, 2023
# purpose:  XX

from body import Body

class System:
    def __init__(self, list_bodies):
        self.bodies = list_bodies
# computes the accelerations on each body and then calls methods in Body to update the velocity and position of each body.
    def update(self, timestep):
        (ax, ay) = self.compute_acceleration(len(self.bodies))
        for bod in self:
            bod.update_position(timestep)
            bod.update_velocity(ax, ay, timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for bod in self.bodies:
            bod.draw(bod.x, bod.y, bod.pixels_per_meter)

    def compute_acceleration(self, n):

        return (a_x, a_y)  # return a tuple with two values, the accelerations in x and y


