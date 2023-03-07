# filename: vertex.py
# author:   Valerie Gadapati
# date:     Mar 7, 2023
# purpose:  define a class Vertex that describes connected vertices and data

from cs1lib import *

NODE_RADIUS = 10
EDGE_WIDTH = 5


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.adj_verts = []
        # x and y coordinates as ints
        self.x = x
        self.y = y

    def __str__(self):
        # logic to not have a comma after the last adjacent vertex
        adj = ""
        for i in range(len(self.adj_verts)):
            elem = self.adj_verts[i]
            if i < len(self.adj_verts) - 1:
                adj += str(elem.name)
                adj += ", "
            else:
                adj += str(elem.name)

        # returns a string in the format of Vertex Name; Location: X, Y; Adjacent vertices: Adj1, Adj2, ... , Adjx
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + adj

    # draw a node as a circle in a given color
    def draw_node(self, r, g, b):
        set_fill_color(r, g, b, 1)
        disable_stroke()

        draw_circle(self.x, self.y, NODE_RADIUS)

    # draw an edge between two nodes as a straight line in a given color
    def draw_edge(self, next, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b, 1)
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, next.x, next.y)

    # visualize all the adjacent edges in a given color
    def draw_all_adj(self, r, g, b):
        for node in self.adj_verts:
            self.draw_edge(node, r, g, b)

    # return whether a given coordinate is within the visual space of a node
    def in_node(self, x, y):
        if (self.x - NODE_RADIUS <= x <= self.x + NODE_RADIUS) and (self.y - NODE_RADIUS <= y <= self.y + NODE_RADIUS):
            return True
        return False
