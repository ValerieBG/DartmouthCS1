## DOCU HERE
from vertex import Vertex


# Your job is to write a function load_graph in load_graph.py, which takes one parameter, the name of the data file.
# load_graph should create one Vertex object per line in the data file and add to a dictionary a reference to each
# Vertex object it creates. The Vertex references (addresses) will be the values in the dictionary, and the
# names of the vertices will be the keys for the dictionary. When done reading and processing all the information
# in the data file, the function should return the address of the dictionary, which will have information about all
# the vertices.
def load_graph(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    data = open(filename, "r")

    for line in data:
        split_params = line.split(";")
        name = split_params[0].strip()
        adj_verts = split_params[1].strip().split(",")  # returns a list
        adj = []
        for x in adj_verts:
            adj.append(x.strip())
        coords = split_params[2].strip().split(",")
        x = coords[0].strip()
        y = coords[1].strip()

        vertex_dict[name] = Vertex(str(name), adj, int(x), int(y))
        # print(vertex_dict[name])  # for testing
    data.close()
    return vertex_dict


load_graph("dartmouth_graph.txt")
