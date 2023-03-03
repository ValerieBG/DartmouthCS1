# filename: vertex.py
# author:   Valerie Gadapati
# date:     Mar 7, 2023
# purpose:  define a class Vertex that describes connected vertices and data

class Vertex:
    def __init__(self, name, adj_verts, x, y):
        self.name = name
        self.adj_verts = adj_verts
        # x and y coordinates as ints
        self.x = x
        self.y = y

    def __str__(self):
        # logic to not have a comma after the last adjacent vertex
        adj = ""
        for i in range(len(self.adj_verts)):
            elem = self.adj_verts[i]
            if i < len(self.adj_verts) - 1:
                adj += str(elem)
                adj += ", "
            else:
                adj += str(elem)

        # returns a string in the format of Vertex Name; Location: X, Y; Adjacent vertices: Adj1, Adj2, ... , Adjx
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + adj