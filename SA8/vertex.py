# filename: vertex.py
# author:   Valerie Gadapati
# date:     Mar 3, 2023
# purpose:  define a class Vertex that describes connected vertices and data

class Vertex:
    def __init__(self):


# A Vertex contains reference to a Python list of strings describing the connected vertices, and some data. For the
# example vertex, the adjacency list would be ["LESS_TRAVELED", "BRIDGE"], and the data would be "You are walking...more-traveled?"
#
# Where are vertices stored? We'll use a dictionary of vertices. The vertex names will be the keys into the dictionary.
# For our example, you'd like something like this: vertices["START"] = Vertex(...) (That's just a hint.
# Your code won't look exactly like this.)