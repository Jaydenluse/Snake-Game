from grid import Grid
from snake import Snake
from constants import BASEPATH
import pygame as game
import os as os

class Game:
    def __init__(self):
        self.score = 0
        self.tokens = 0
        self.grid = Grid()
        self.snake = Snake()

    def runLoop(self) -> None:
        if self.score % 10 == 0 and self.score > 0:
            if not sound_played:
                game.mixer.music.load(os.path.join(BASEPATH, 'Assets/snake pause.wav'))
                game.mixer.music.play(0)
                button_screen()
                sound_played = True
            framerate = framerate + 5
            if_statement_run = True
            pause_game = True