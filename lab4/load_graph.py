# filename: load_graph.py
# author:   Valerie Gadapati
# date:     Mar 7, 2023
# purpose:  parse a file to create a dictionary of locational information

from vertex import Vertex


# function to parse a data file and create a dictionary of vertices from it
def load_graph(filename):

    vertex_dict = {}

    # read the data file
    data = open(filename, "r")

    for line in data:
        # first split by ; into three categories
        split_params = line.split(";")

        # identify the name of the vertex
        name = split_params[0].strip()

        # identify the x and y coordinates
        coords = split_params[2].strip().split(",")
        x = coords[0].strip()
        y = coords[1].strip()

        # add the new vertex to a dictionary using appropriate parameters
        vertex_dict[name] = Vertex(str(name), int(x), int(y))
        # print(vertex_dict[name])  # for testing
    data.close()

    # second round of analysis to grab adjacent vertices as objects
    data = open(filename, "r")
    for line in data:
        # first split by ; into three categories
        split_params = line.split(";")
        # identify the name of the vertex
        name = split_params[0].strip()
        adj_verts = split_params[1].strip().split(",")  # returns a list
        for x in adj_verts:
            vertex_dict[name].adj_verts.append(vertex_dict[x.strip()])
        # print(vertex_dict[name])  # for testing

    data.close()
    return vertex_dict


load_graph("dartmouth_graph.txt")
