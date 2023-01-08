print("Hello")

print("Hello")
print("my")
print("name")
print("is")
print("Inigo")
print("Montoya")

def say_hello():
    print("Hello.")

def why_goodbye():
    print("I don't know why you say goodbye.")

say_hello()
say_hello()
why_goodbye()
print("I say hello.")

#Objective: Write and call your own functions to learn how the program counter steps through code.
def print_favorite_number():
    print("7")

def say_introduction():
    print("Hello, my name is Anna.")
    print("I am a Banana.")

say_introduction()
print_favorite_number()

#Objective: learn how to call drawing library functions that take parameters, in order to draw a desired complex picture.
from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

def draw():

    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0) #set yellow
    draw_circle(200, 200, 150)

    # draw the mouth
    draw_circle(200, 200, 50)
    set_fill_color(1, 1, 0)
    set_stroke_color(1, 1, 0)
    draw_rectangle(100, 130, 200, 70)

    # draw the eyes
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 0, 0) #set black
    draw_circle(150, 150, 10) #L eye
    draw_circle(250, 150, 10) #R eye

start_graphics(draw)