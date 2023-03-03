# DOCU

class Vertex:
    def __init__(self, name, adj_verts, x, y):
        self.adj_verts = adj_verts
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        adj = ""
        for i in range(len(self.adj_verts)):
            elem = self.adj_verts[i]
            if i < len(self.adj_verts) - 1:
                adj += str(elem)
                adj += ", "
            else:
                adj += str(elem)
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + adj