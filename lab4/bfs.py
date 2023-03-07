# filename: bfs.py
# author:   Valerie Gadapati
# date:     Mar 7, 2023
# purpose:  initiate breadth first search given a start and end node

from collections import deque


def breadth_first_search(start, goal):
    path = []  # list of vertices to represent the path
    q = deque()  # frontier, first in first out
    q.append(start)
    backpointers = {start: None}  # value for a particular key (vertex) is its backpointer (vertex)

    while len(q) > 0:
        curr_vert = q.popleft()

        for vert in curr_vert.adj_verts:
            if vert not in backpointers:
                backpointers[vert] = curr_vert
                q.append(vert)

        # once the end of the path is reached, generate the path by going through the backpointers
        if curr_vert == goal:
            placeholder = goal
            path.append(goal)
            while placeholder != start:
                placeholder = backpointers[placeholder]
                path.append(placeholder)

    return path
