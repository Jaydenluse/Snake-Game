import os
import pygame as game

game.mixer.init()
game.font.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215,0)
TRANSPARENT = (255, 255, 255, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

WINDOW_SIZE = [1000, 1000]

# This sets the margin between each cell
MARGIN = 3

UP = "UP"
LEFT = "LEFT"
RIGHT = "RIGHT"
DOWN = "DOWN"

BASEPATH = os.path.dirname(__file__)

BASEFONT = os.path.join(BASEPATH, "Assets/8Bit.ttf")

FONT = lambda size : game.font.Font(BASEFONT, size)

H1 = FONT(150)
H2 = FONT(100)
H3 = FONT(75)
H4 = FONT(45)
H5 = FONT(35)
H6 = FONT(25)

SAVEFILE1 = os.path.join(BASEPATH, 'Snake/snake1.pickle')
SAVEFILE2 = os.path.join(BASEPATH, 'Snake/snake2.pickle')
SAVEFILE3 = os.path.join(BASEPATH, 'Snake/snake3.pickle')