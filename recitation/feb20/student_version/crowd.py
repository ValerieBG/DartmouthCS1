# my class file for recitation feb 20

from random import *
from face import *
class Crowd:
    def __init__(self, num_faces):
        self.face_count = num_faces
        self.faces = []

        i = 0
        while i <= num_faces:
            f = Face(randint(0, 400), randint(0, 400), 20)
            self.faces.append(f)
            i += 1

    def lookat(self, mx, my):
        for face in self.faces:
            face.lookat(mx, my)

    def draw(self):
        for face in self.faces:
            face.draw()
