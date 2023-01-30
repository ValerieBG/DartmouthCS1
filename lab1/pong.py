# filename: pong.py
# author:   Valerie Gadapati
# date:     Jan 28, 2023
# purpose:  create a functional game of pong for 2 players using a keyboard

# EC IDEAS: display names/initials and points

from cs1lib import *

WINDOW_X = 400  # The height of the window.
WINDOW_Y = 400  # the width of the window
PADDLE_WIDTH = 20  # the width of the paddle
PADDLE_HEIGHT = 80  # the height of the paddle

LEFT_UP_KEY = 'a'
LEFT_DOWN_KEY = 'z'
RIGHT_UP_KEY = 'k'
RIGHT_DOWN_KEY = 'm'
START_KEY = ' '
QUIT_KEY = 'q'

PADDLE_INCREMENT = 5  # The amount that a paddle moves when it moves.

BALL_RADIUS = 10
X_BALL_INCREMENT = 1
Y_BALL_INCREMENT = 1

# start screen that tells the user to hit space to start the game
def start_screen():
    global default, left_paddle_y, left_paddle_x, right_paddle_x, right_paddle_y  # global variable to make sure the canvas doesn't constantly loop and clear states

    set_clear_color(0, 0, 0, 1)  # set background black

    if default:
        clear()
        set_stroke_color(1, 1, 1, 1)
        draw_text("welcome to pongggg hit space 2 start spacegeek", WINDOW_X // 6, WINDOW_Y // 2)
        left_paddle_x = 0
        left_paddle_y = 0
        right_paddle_x = WINDOW_X - PADDLE_WIDTH
        right_paddle_y = WINDOW_Y - PADDLE_HEIGHT
        default = False  # change state to false, so it only runs once in the beginning

# set board background for game play with a white dashed line divider
def playing_screen():
    global ball_x, ball_y
    # draw dotted divider line
    dash_y = 0
    dash_width = 5
    while dash_y <= WINDOW_Y:
        dash_x = WINDOW_X // 2 - dash_width//2
        set_stroke_color(1, 1, 1, 1)
        set_fill_color(1, 1, 1, 1)
        draw_rectangle(dash_x, dash_y, dash_width, 10)
        dash_y = dash_y + 20

def keypress(key):
    global playing, default, pressed_left_up, pressed_left_down, pressed_right_up, pressed_right_down, ball_x

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
        cs1_quit()

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
    global playing, default, left_paddle_y, right_paddle_y

    # left paddle movement
    if left_paddle_y > 0:
        if pressed_left_up:
            left_paddle_y = left_paddle_y - PADDLE_INCREMENT

    if left_paddle_y < WINDOW_Y - PADDLE_HEIGHT:
        if pressed_left_down:
            left_paddle_y = left_paddle_y + PADDLE_INCREMENT

    # right paddle movement
    if right_paddle_y > 0:
        if pressed_right_up:
            right_paddle_y = right_paddle_y - PADDLE_INCREMENT

    if right_paddle_y < WINDOW_Y - PADDLE_HEIGHT:
        if pressed_right_down:
            right_paddle_y = right_paddle_y + PADDLE_INCREMENT

def move_ball():
    global ball_x, ball_y, X_BALL_INCREMENT, Y_BALL_INCREMENT
    ball_x = ball_x + X_BALL_INCREMENT
    ball_y = ball_y + (Y_BALL_INCREMENT * 2)

def ball_behavior():
    global ball_x, ball_y, BALL_RADIUS, X_BALL_INCREMENT, Y_BALL_INCREMENT, right_paddle_x, right_paddle_y, left_paddle_x, left_paddle_y, PADDLE_HEIGHT, PADDLE_WIDTH
    # behavior to bounce off the vertical top and bottom walls
    if ((ball_y - BALL_RADIUS) <= 0) or ((ball_y + BALL_RADIUS) >= WINDOW_Y):
        Y_BALL_INCREMENT = -Y_BALL_INCREMENT

    if ((ball_x + BALL_RADIUS) >= WINDOW_X) or ((ball_x-BALL_RADIUS) <= 0):
        # NEED A BETTER WAY TO DO THESE RESETS!!! create a function or something that wouldn't interfere with points
        ball_x = WINDOW_X // 2
        ball_y = WINDOW_Y // 2
        X_BALL_INCREMENT = 1
        Y_BALL_INCREMENT = 1

    # if it hits the right paddle, y direction same, x component flips
    # conditions: ball rightmost edge >= inner edge of paddle and ball y pos is within the paddle top and bottom)
    if (ball_x + BALL_RADIUS >= right_paddle_x) and (right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT):
        X_BALL_INCREMENT = -X_BALL_INCREMENT

    # if it hits the left paddle, y direction same, x component flips
    if (ball_x - BALL_RADIUS <= left_paddle_x + PADDLE_WIDTH) and (left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT):
        X_BALL_INCREMENT = -X_BALL_INCREMENT
def graphics():
    global playing
    if default:
        start_screen()  # initialize the board to its default state

    if playing:
        clear()
        playing_screen()
        draw_rectangle(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # left paddle
        draw_rectangle(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)  # right paddle
        move_paddles()

        draw_circle(ball_x, ball_y, BALL_RADIUS)
        move_ball()
        ball_behavior()

# state variables
playing = False
default = True

left_paddle_x = 0
left_paddle_y = 0
right_paddle_x = WINDOW_X - PADDLE_WIDTH
right_paddle_y = WINDOW_Y - PADDLE_HEIGHT

pressed_left_up = False
pressed_left_down = False
pressed_right_up = False
pressed_right_down = False

ball_x = WINDOW_X//2
ball_y = WINDOW_Y//2
# utilize callback functions to check keyboard inputs for gameplay
start_graphics(graphics, 2400, key_press=keypress, key_release=keyrelease)
