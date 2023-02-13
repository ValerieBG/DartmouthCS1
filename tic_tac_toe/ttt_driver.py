# filename: pong.py
# author:   Valerie Gadapati
# date:     Feb 3, 2023
# purpose:  create a functional game of pong for 2 players using keyboard inputs

from cs1lib import *

WINDOW_X = 400  # The height of the window.
WINDOW_Y = 400  # the width of the window

START_KEY = ' '
QUIT_KEY = 'q'

PADDLE_INCREMENT = 5  # The amount that a paddle moves when it moves.

BALL_RADIUS = 10
X_BALL_INCREMENT = 1  # x distance component of balls movement
Y_BALL_INCREMENT = 1  # y distance component of balls movement


# create a start screen that tells the user to hit space to start the game
def start_screen():
    global default, left_paddle_y, left_paddle_x, right_paddle_x, right_paddle_y, ball_x, ball_y

    set_clear_color(0, 0, 0, 1)  # set background black

    if default:
        # create a welcome screen
        clear()
        set_stroke_color(1, 1, 1, 1)
        set_font_size(20)
        draw_text("welcome to pong! hit space to start", WINDOW_X // 8, WINDOW_Y // 2)

        # set initial paddle locations in opposite corners
        left_paddle_x = 0
        left_paddle_y = 0
        right_paddle_x = WINDOW_X - PADDLE_WIDTH
        right_paddle_y = WINDOW_Y - PADDLE_HEIGHT

        # set initial ball location
        ball_x = WINDOW_X // 2
        ball_y = WINDOW_Y // 2

        # change state to false, so it only runs on start up
        default = False


# set board background for game play with a white dashed line divider
def playing_screen():
    global ball_x, ball_y

    dash_y = 0
    dash_width = 5

    # for the length of the window draw evenly spaced rectangles
    while dash_y <= WINDOW_Y:
        dash_x = WINDOW_X // 2 - dash_width//2
        set_stroke_color(1, 1, 1, 1)
        set_fill_color(1, 1, 1, 1)
        draw_rectangle(dash_x, dash_y, dash_width, 10)
        dash_y = dash_y + 20

# detect when a key is pressed
def keypress(key):
    global playing, default

    if key == START_KEY:
        playing = True
        default = False

    if key == QUIT_KEY:
        playing = False
        default = True
        cs1_quit()  # closes game window entirely, comment out to only return to start screen

# function to check mouse being pressed
def press(mx, my):
    global draw, old_x, old_y
    old_x = mx  # the starting position of the line should be when it is pressed
    old_y = my
    draw = True  # if the mouse is pressed, drawing should be occurring

def release(mx, my):
    global draw
    draw = False  # when the mouse is released, no more drawing should be occurring

def move(mx, my):
    global curr_x, curr_y
    curr_x = mx  # as the mouse moves, set its new value to be used to draw a line
    curr_y = my

# main function to run the game
def graphics():
    global playing
    if default:
        start_screen()  # initialize the board to its default state

    if playing:
        clear()
        playing_screen()


# state variables
old_x = 0
old_y = 0
curr_x = 0
curr_y = 0
draw = False
default = True

# state variables
playing = False
default = True


# utilize callback functions to check keyboard inputs and facilitate gameplay
start_graphics(graphics, 2400, mouse_press=press, mouse_release=release, mouse_move=move, key_press=keypress)