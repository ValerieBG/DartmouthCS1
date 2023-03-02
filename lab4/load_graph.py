## DOCU HERE
from vertex import Vertex


# Your job is to write a function load_graph in load_graph.py, which takes one parameter, the name of the data file.
# load_graph should create one Vertex object per line in the data file and add to a dictionary a reference to each
# Vertex object it creates. The Vertex references (addresses) will be the values in the dictionary, and the
# names of the vertices will be the keys for the dictionary. When done reading and processing all the information
# in the data file, the function should return the address of the dictionary, which will have information about all
# the vertices.

def load_graph(data):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(data, "r")

    for l in file:
        l = l.strip()
        vertex_name = l.split(";")[0]
        adj_verts = l.split(";")[1]
        adj_verts = adj_verts.split(",")
        vertex_dict[vertex_name] = Vertex(vertex_name, adj_verts)
    file.close()
