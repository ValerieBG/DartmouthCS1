# filename: adventure.py
# author:   Vasanta Lakshmi Kommineni & Valerie Gadapati
# date:     Mar 3, 2023
# purpose:  display a choose your own adventure game given a text file

from vertex import Vertex


def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            print("vertex " + vertex_name)
            print(" adjacent:  " + str(adjacent_vertices))
            print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
        vertex_dict[vertex_name] = Vertex(vertex_name, adjacent_vertices, text)

    file.close()

    return vertex_dict

# Finally, write a function containing a while loop that allows you to play the game. Grab the vertex "START" from the
# dictionary, get the list of choices, and allow the user to input a value like a, b, or c using the Python input
# function, which you may look up online. (If you are using Python 2, you should use the function raw_input instead.)
# Based on that choice (remember you can convert a char to a number using ord), grab the next vertex from the
# dictionary, and repeat until you reach a vertex with no outgoing links.
def play_game(dict):
    alive = True
    curr_vertex = dict["START"]

    while alive:
        print(curr_vertex.text)



# Your code for adventure.py should call the function to start game play after loading the story data into the graph.
story_dict = load_story("story.txt")
play_game(story_dict)
