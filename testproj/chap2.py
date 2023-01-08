greeting = "hello"
print(greeting)
# print(hello) is invalid
print("greeting")
print("hello")

from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

def draw():

    x = 100
    y = 100
    scale = 1

    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0)   # set fill color to yellow
    draw_circle(x, y, 50*scale)

    # draw the mouth
    set_fill_color(1, 1, 0)  # yellow
    draw_circle(x, y, 30)
    set_stroke_color(1, 1, 0)
    draw_rectangle(x - 32, y - 32, 62, 40)

    # draw the eyes
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 0, 0)  # set fill color to black
    draw_circle(x - 20, y - 10, 5)
    draw_circle(x + 20, y - 10, 5)

start_graphics(draw)