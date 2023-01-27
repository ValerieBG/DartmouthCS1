# filename: pong.py
# author:   Valerie Gadapati
# date:     Jan 28, 2023
# purpose:  create a functional game of pong for 2 players using a keyboard

# EC IDEAS: display names/initials and points

from cs1lib import *

WINDOW_X = 400  # The height of the window.
WINDOW_Y = 400  # the width of the window
PADDLE_X = 20  # the width of the paddle
PADDLE_Y = 80  # the height of the paddle

LEFT_UP_KEY = 'a'
LEFT_DOWN_KEY = 'z'
RIGHT_UP_KEY = 'k'
RIGHT_DOWN_KEY = 'm'
START_KEY = ' '
QUIT_KEY = 'q'

PADDLE_INCREMENT = 5  # The amount that a paddle moves when it moves.

# start screen that tells the user to hit space to start the game
def start_screen():
    global default, left_y, left_x, right_x, right_y  # global variable to make sure the canvas doesn't constantly loop and clear states

    set_clear_color(0, 0, 0, 1)  # set background black

    if default:
        clear()
        set_stroke_color(1, 1, 1, 1)
        draw_text("welcome to pongggg hit space 2 start spacegeek", WINDOW_X // 6, WINDOW_Y // 2)
        left_x = 0
        left_y = 0
        right_x = WINDOW_X - PADDLE_X
        right_y = WINDOW_Y - PADDLE_Y
        default = False  # change state to false, so it only runs once in the beginning

# set board background for game play with a white dashed line divider
def playing_screen():
    # draw dotted divider line
    dash_y = 0
    while dash_y <= WINDOW_Y:
        dash_x = WINDOW_X // 2
        set_stroke_color(1, 1, 1, 1)
        set_fill_color(1, 1, 1, 1)
        draw_rectangle(dash_x, dash_y, 5, 10)
        dash_y = dash_y + 20

def keypress(key):
    global playing, default, pressed_left_up, pressed_left_down, pressed_right_up, pressed_right_down

    if key == LEFT_UP_KEY:
        pressed_left_up = True
    if key == LEFT_DOWN_KEY:
        pressed_left_down = True

    if key == RIGHT_UP_KEY:
        pressed_right_up = True
    if key == RIGHT_DOWN_KEY:
        pressed_right_down = True

    if key == START_KEY:
        playing = True

    if key == QUIT_KEY:
        playing = False
        default = True

# if a key is released, stop moving the paddle
def keyrelease(key):
    global pressed_left_down, pressed_left_up, pressed_right_up, pressed_right_down
    if key == LEFT_UP_KEY:
        pressed_left_up = False
    if key == LEFT_DOWN_KEY:
        pressed_left_down = False
    if key == RIGHT_UP_KEY:
        pressed_right_up = False
    if key == RIGHT_DOWN_KEY:
        pressed_right_down = False

# function to change the position of the paddles based on keyboard input
def move_paddles():
    global playing, default, left_y, right_y

    # left paddle movement
    if left_y > 0:
        if pressed_left_up:
            left_y = left_y - PADDLE_INCREMENT

    if left_y < WINDOW_Y - PADDLE_Y:
        if pressed_left_down:
            left_y = left_y + PADDLE_INCREMENT

    # right paddle movement
    if right_y > 0:
        if pressed_right_up:
            right_y = right_y - PADDLE_INCREMENT

    if right_y < WINDOW_Y - PADDLE_Y:
        if pressed_right_down:
            right_y = right_y + PADDLE_INCREMENT

def graphics():
    global playing
    if default:
        start_screen()  # initialize the board to its default state

    if playing:
        clear()
        playing_screen()
        draw_rectangle(left_x, left_y, PADDLE_X, PADDLE_Y)  # left paddle
        draw_rectangle(right_x, right_y, PADDLE_X, PADDLE_Y)  # right paddle
        move_paddles()

# state variables
left_x = 0
left_y = 0
right_x = WINDOW_X - PADDLE_X
right_y = WINDOW_Y - PADDLE_Y

playing = False
default = True

pressed_left_up = False
pressed_left_down = False
pressed_right_up = False
pressed_right_down = False

# utilize callback functions to check keyboard inputs for gameplay
start_graphics(graphics, 2400, key_press=keypress, key_release=keyrelease)
