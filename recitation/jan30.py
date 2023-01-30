# filename: jan30.py
# author:   Valerie Gadapati
# date:     Jan 30, 2023
# purpose:  to draw a circle that moves

from cs1lib import *

LEFT_KEY = 'l'
RIGHT_KEY = 'r'

BALL_RADIUS = 20
X_BALL_INCREMENT = 5

def keypress(key):
    global pressed_left, pressed_right

    if key == LEFT_KEY:
        pressed_left = True
    if key == RIGHT_KEY:
        pressed_right = True

def keyrelease(key):
    global pressed_left, pressed_right
    if key == LEFT_KEY:
        pressed_left = False
    if key == RIGHT_KEY:
        pressed_right = False
def move_ball():
    global ball_x

    if pressed_left:
        ball_x = ball_x + X_BALL_INCREMENT
    if pressed_right:
        ball_x = ball_x - X_BALL_INCREMENT
def graphics():
    global playing
    clear()

    set_fill_color(1,0,0,1)
    set_stroke_color(1,0,0,1)
    move_ball()
    draw_circle(ball_x, ball_y, BALL_RADIUS)

pressed_left = False
pressed_right = False

ball_x = 400//2
ball_y = 400//2

# utilize callback functions to check keyboard inputs for movement
start_graphics(graphics, 2400, key_press=keypress, key_release=keyrelease)
