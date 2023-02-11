import pygame
import random
import os
import time
import pickle # Will use to save later
import constants
from grid import Grid, CellType
from helpers import transformTypeToColor
from display import Display, DisplayType
from constants import SAVEFILE1, SAVEFILE2, SAVEFILE3, WHITE, BLACK, HEIGHT, WIDTH, MARGIN
from variables import Variables

base_path = os.path.dirname(__file__)

elapsed_time = 0
count = 0
game_loaded = False
FONT = os.path.join(base_path, "Assets/8Bit.ttf")
pygame.mixer.init()
pygame.font.init()

grid = Grid()

display = Display()

def save_game(file_path, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run):
    print(file_path)
    print(score)
    with open(file_path, "wb") as file:
        data = (snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run)
        pickle.dump(data, file)

def load_game(file_path):
    with open(file_path, "rb") as file:
        # Load the binary file and restore the grid, score, and food_location variables
        snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run = pickle.load(file)
    return snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run

# def save_screen():

def remove_parts():
    snake_body = len(snake.body)
    while len(snake.body) >= snake_body - 2:
        snake.body = snake.body[:-1]

def slow_snake():
    variables.framerate = variables.framerate - 5

def multiply_score():
    variables.multiplier = variables.multiplier * 2

class Snake:
    def __init__(self):
        print('nope')
        self.body = [(9, 6), (9, 7), (9, 8)]
        self.direction = "UP"
        self.score = 0
        self.tokens = 0

    def changeDirection(self, direction):
        print(direction)
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def move(self):
        y, x = self.body[0]

        if self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "RIGHT":
            x += 1

        self.body.insert(0, (y, x))

        # If the snake did not eat any food, remove the last part of the body
        if (x, y) != food_pos:
            self.body.pop()

    def check_collision(self):
        # Check if the snake hit a wall or itself
        x, y = self.body[0]

        if x < 0 or x > 19 or y < 0 or y > 19:
            return True
        if self.body[0] in self.body[1:]:
            return True

        return False

    def check_food(self):
        # Check if the snake ate the food
        if self.body[0] == food_pos and (self.score % 3 != 0 or self.score == 0):
            self.score += 1
            return True

        return False

    def check_token(self):
        if self.body[0] == token_pos and self.score and self.score % 3 == 0 and self.score != 0:
            self.score += 1
            self.tokens += 1
            return True
        
        return False

# Initialize pygame
pygame.init()

# Set display dimensions
display_width = 600
display_height = 600

# Initialize game display
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.mixer.music.load(os.path.join(base_path, 'Assets/snake loop.wav'))

variables = Variables()

pause_game = True

elapsed_time = 0
variables.framerate = 20
variables.multiplier = 1
food_counter = 0
body_count = 0
snake = Snake()
food_pos = (random.randint(0, 19), random.randint(0, 19))
token_pos = (random.randint(0, 19), random.randint(0, 19))

# Define font
font = pygame.font.Font(FONT, 45)        
font2 = pygame.font.Font(FONT, 150)
font3 = pygame.font.Font(FONT, 25)
home_font = pygame.font.Font(FONT, 150)
home_font2 = pygame.font.Font(FONT, 45)

# Set the HEIGHT and WIDTH of the screen
display.initDisplay()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
given_reward = False
sound_played = False
while not done:
    # GOLD FOOD BLOCK
    if not given_reward and snake.score % 2 == 0 and snake.score > 0:
        if not sound_played:
            pygame.mixer.music.load(os.path.join(base_path, 'Assets/snake pause.wav'))
            pygame.mixer.music.play(0)
            display.showRewardScreen()
            sound_played = True
        variables.framerate = variables.framerate + 5
        given_reward = True
        pause_game = True

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if pause_game:
                pygame.mixer.music.play(-1)
                pause_game = False
            if event.key == pygame.K_TAB:
                print(score)
                display.showPauseScreen()
            if event.key == pygame.K_UP:
                snake.changeDirection("UP")
            elif event.key == pygame.K_DOWN:
                snake.changeDirection("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.changeDirection("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.changeDirection("RIGHT")
        elif given_reward and snake.score % 10 == 0:
            given_reward = False
            sound_played = False

    # --- Game logic should go here

    if not pause_game:
        snake.move()
        elapsed_time += clock.tick(variables.framerate) / 1000.0
        pygame.mixer.music.load(os.path.join(base_path, 'Assets/snake loop.wav'))
        pygame.mixer.music.play(-1)

    if snake.check_collision():
        print('collision')
        pygame.mixer.music.load(os.path.join(base_path, 'Assets/snake collision.wav'))
        pygame.mixer.music.play(0)
        variables.framerate = 20
        elapsed_time = 0
        variables.multiplier = 1
        food_pos = (random.randint(0, 19), random.randint(0, 19))
        pause_game = True
        food_counter = 0
        body_count = 0
        snake = Snake()

    quicker = snake.score % 10 == 0 and snake.score != 0

    if snake.check_food():
        print('check')
        food_counter += variables.multiplier
        pygame.mixer.music.load(os.path.join(base_path, 'Assets/snake loop food.wav'))
        pygame.mixer.music.play(0)
        while (snake.score % 3 != 0 or snake.score == 0):
            food_pos = (random.randint(0, 19), random.randint(0, 19))
            if food_pos not in snake.body:
                break

    if snake.check_token():
        food_counter += 1
        pygame.mixer.music.load(os.path.join(base_path, 'Assets/token.wav'))
        pygame.mixer.music.play(0)
        while snake.score % 3 == 1 and snake.score != 0:
            token_pos = (random.randint(0, 19), random.randint(0, 19))
            if token_pos not in snake.body and token_pos != food_pos:
                break

    # Get score
    score = food_counter

    if display.getCurrentDisplay() == DisplayType.Home:
        display.showHomeScreen()
    else:
        grid.resetGrid()
        grid.reserveCells(snake.body, CellType.SNAKE)
        display.showGameScreen(grid, food_pos, score, elapsed_time, snake)
   
    if game_loaded:
        snake, variables.framerate, variables.multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, given_reward = load_game(file)
        game_loaded = False

    pygame.display.update()

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(variables.framerate)