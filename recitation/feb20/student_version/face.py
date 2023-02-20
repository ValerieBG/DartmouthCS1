from cs1lib import *
from eye import Eye

class Face:
    def __init__(self, x, y, size):
        # face position and size
        self.x = x
        self.y = y
        self.size = size
        
        # create eyes
        ex1 = int(x-0.3*size)
        ey1 = int(y-0.3*size)
        self.lefteye = Eye(ex1, ey1, size//5)

        ex2 = int(x+0.3*size)
        ey2 = int(y-0.3*size)
        self.righteye = Eye(ex2, ey2, size//5)
        
    def lookat(self, lx, ly):
        self.lefteye.lookat( lx, ly )
        self.righteye.lookat( lx, ly )
       
    def draw(self):
        enable_stroke()
        set_fill_color(1,1,1)
        draw_circle(self.x, self.y, self.size) # draw face
        self.lefteye.draw() # draw eyes
        self.righteye.draw() # draw eyes
        draw_line(self.x, self.y, self.x, int(self.y+0.3*self.size))  # draw nose
        draw_line(int(self.x-0.3*self.size), int(self.y+0.4*self.size), \
                   int(self.x+0.3*self.size), int(self.y+0.4*self.size)) # draw mouth