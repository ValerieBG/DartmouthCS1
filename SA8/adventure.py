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

            #print("vertex " + vertex_name)
            #print(" adjacent:  " + str(adjacent_vertices))
            #print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
        vertex_dict[vertex_name] = Vertex(vertex_name, adjacent_vertices, text)

    file.close()

    return vertex_dict


# function to play the choose-your-own-adventure game
def play_game(dict):
    active = True
    curr_vertex = dict["START"]

    while active:
        print(curr_vertex.text)
        # if there is a possible choice continue the story
        if len(curr_vertex.adj_vertices) > 0:
            # turn the letter typed into a corresponding index
            user_choice = ord(input("Type your choice: ")) - ord("a")
            # if the user enters an option not presented, prompt them again
            while user_choice > len(curr_vertex.adj_vertices) - 1:
                print("Not an option! Try again...")
                user_choice = ord(input("Type your choice: ")) - ord("a")
            curr_vertex = dict[curr_vertex.adj_vertices[user_choice]]
        # if reached an end of story, aka a node w no adjacent vertices, exit the game
        else:
            active = False


# load the story data into the graph
story_dict = load_story("story.txt")
# call the function to start game play
play_game(story_dict)
