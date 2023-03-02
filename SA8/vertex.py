# filename: vertex.py
# author:   Valerie Gadapati
# date:     Mar 3, 2023
# purpose:  define a class Vertex that describes connected vertices and data

class Vertex:
    def __init__(self, name, adj_vertices, text):
        self.name = name
        self.adj_vertices = adj_vertices
        self.text = text
