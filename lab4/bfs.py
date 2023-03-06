## DOCU HERE

from collections import deque

def breadth_first_search(start, goal):
    path = []  # Represent the path by a Python list of references to Vertex objects for all vertices on the path.
    q = deque()  # frontier, first in first out
    q.append(start)
    backpointers = {start: None}  # value for a particular key (vertex) is its backpointer (vertex)

    while len(q) > 0:
        curr_vert = q.popleft()

        for vert in curr_vert.adj_verts:
            if vert not in backpointers:
                backpointers[vert] = curr_vert
                q.append(vert)

        if curr_vert == goal:
            placeholder = goal
            path.append(goal)
            while placeholder != start:
                placeholder = backpointers[placeholder]
                path.append(placeholder)

    return path
