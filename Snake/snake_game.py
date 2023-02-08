import pygame
import random
import os
import time
import pickle 
import sys
# from snake_class import Snake 

file_path1 = '/Users/apple/Snake-Game/Snake/snake1.pickle'
file_path2 = '/Users/apple/Snake-Game/Snake/snake2.pickle'
file_path3 = '/Users/apple/Snake-Game/Snake/snake3.pickle'




start_noise = '/Users/apple/Snake-Game/Snake/Assets/start noise1.wav'


elapsed_time = 0
count = 0
homescreen = True
game_loaded = False
FONT = "/Users/apple/Snake-Game/Snake/Assets/8Bit.ttf"
pygame.mixer.init()
pygame.font.init()


y1 = 0
y2 = 0
y3 = 0

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

# This sets the margin between each cell
MARGIN = 3


def home_screen():   
    while True:
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake music.wav')
        pygame.mixer.music.play(-1)
        global homescreen 
        home_screen_surface = pygame.Surface((1000, 1000))
        pygame.draw.rect(gameDisplay, BLACK, (500, 500, 500, 500), 0)
        background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/main_screen2.png')
        button_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/button_background_background.png')
        game_text = font2.render("SNAKE", True, WHITE)
        start_button = font.render("New Game", True, WHITE)
        load_button = font.render("Load Game", True, WHITE)
        token_shop = font.render("Token Shop", True, WHITE)
        game_info = font.render("Game Info", True, WHITE)

        home_screen_surface.blit(button_background, [0,-35])
        home_screen_surface.blit(background, [0,-35])
        home_screen_surface.blit(game_text, [305, 25])
        home_screen_surface.blit(start_button, [420, 240])
        home_screen_surface.blit(load_button, [415, 380])
        home_screen_surface.blit(token_shop, [405, 520])
        home_screen_surface.blit(game_info, [415, 660])

        gameDisplay.blit(home_screen_surface, (0, 0))
        pygame.display.update()
        load_game_bool = True

        while load_game_bool:
            event = pygame.event.wait()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if 420 + 300 > mouse[0] > 420 and 240 + 80 > mouse[1] > 240: #START GAME
                    pygame.mixer.music.load(start_noise)
                    pygame.mixer.music.play(0)
                    homescreen = False
                    return
                if 415 + 300 > mouse[0] > 415 and 380 + 80 > mouse[1] > 380: #LOAD GAME
                    save_file1 = font.render(f'File 1:', True, (255, 255, 255))
                    save_file2 = font.render(f'File 2:', True, (255, 255, 255))
                    save_file3 = font.render(f'File 3:', True, (255, 255, 255))

                    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen.png')
                    sub_screen = pygame.Surface((1000,1000))
                    sub_screen.fill(BLACK)
                    gameDisplay.blit(sub_screen, (0, 0))
                    gameDisplay.blit(button_background, [0,-35])
                    gameDisplay.blit(background, [0,-35])
                    gameDisplay.blit(game_text, [305, 25])
                    gameDisplay.blit(start_button, [420, 240])
                    gameDisplay.blit(pause_background, [0, -35])
                    gameDisplay.blit(save_file1, (390,390))
                    gameDisplay.blit(save_file2, (390,490))
                    gameDisplay.blit(save_file3, (390,590))

                    gameDisplay.blit(save_file1_tokens, (500,415))
                    gameDisplay.blit(save_file1_score, (500,380))

                    gameDisplay.blit(save_file2_tokens, (500,515))
                    gameDisplay.blit(save_file2_score, (500,480))

                    gameDisplay.blit(save_file3_tokens, (500,615))
                    gameDisplay.blit(save_file3_score, (500,580))

                    pygame.mixer.music.load(start_noise)
                    pygame.mixer.music.play(0)
                    pygame.display.update()
                


                    pause = True
                    file_path = None

                    while pause:
                        for event in pygame.event.get():
                            mouse = pygame.mouse.get_pos()
                            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                if 478 + 110 > mouse[0] > 478 and 387 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.load(start_noise)
                                    pygame.mixer.music.play(0)
                                    homescreen = False
                                    global game_loaded
                                    game_loaded = True
                                    file_path = file_path1
                                    return file_path
                                elif 478 + 110 > mouse[0] > 478 and 487 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.load(start_noise)
                                    pygame.mixer.music.play(0)
                                    homescreen = False
                                    game_loaded = True                                
                                    file_path = file_path2
                                    return file_path
                                elif 478 + 110 > mouse[0] > 478 and 587 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.load(start_noise)
                                    pygame.mixer.music.play(0)
                                    homescreen = False
                                    game_loaded = True                               
                                    file_path = file_path3
                                    return file_path
                            if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB or event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                                pause = False
                                load_game_bool = False


def pause_screen():

    home = False

    pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake pause.wav')
    pygame.mixer.music.play(0)

    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen.png')
    sub_screen = pygame.Surface((395, 395))
    sub_screen.fill(BLACK)
    gameDisplay.blit(sub_screen, [310, 310])
    gameDisplay.blit(pause_background, [0, -35])

    font = pygame.font.Font(FONT, 35)
    speed = font.render(f'Speed:     {framerate}', True, WHITE)
    links = font.render(f'Links:     {len(snake.body)}', True, WHITE)
    multiplier_text = font.render(f'Multiplier:     {multiplier} x', True, WHITE)
    save_text = font.render(f'Save Game', True, WHITE)
    home_text = font.render(f'Exit to Home', True, WHITE)
    gameDisplay.blit(speed, (430,365))
    gameDisplay.blit(links, (440,440))
    gameDisplay.blit(multiplier_text, (410,515))
    gameDisplay.blit(save_text, (430,590))
    gameDisplay.blit(home_text, (420,870))
    pygame.display.update()



    pause = True

    while pause:
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 430 + 300 > mouse[0] > 430 and 870 + 80 > mouse[1] > 870: #GO BACK HOME
                    home = True
                    pause = False
                if 430 + 300 > mouse[0] > 420 and 590 + 80 > mouse[1] > 590: #SAVE GAME
                    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen.png')
                    sub_screen = pygame.Surface((395, 395))
                    sub_screen.fill(BLACK)
                    gameDisplay.blit(sub_screen, [310, 310])
                    gameDisplay.blit(pause_background, [0, -35])
                    save_file1 = font.render(f'File 1:', True, (255, 255, 255))
                    save_file2 = font.render(f'File 2:', True, (255, 255, 255))
                    save_file3 = font.render(f'File 3:', True, (255, 255, 255))


                    gameDisplay.blit(save_file1, (390,390))
                    gameDisplay.blit(save_file2, (390,490))
                    gameDisplay.blit(save_file3, (390,590))

                    gameDisplay.blit(save_file1_tokens, (500,415))
                    gameDisplay.blit(save_file1_score, (500,380))

                    gameDisplay.blit(save_file2_tokens, (500,515))
                    gameDisplay.blit(save_file2_score, (500,480))

                    gameDisplay.blit(save_file3_tokens, (500,615))
                    gameDisplay.blit(save_file3_score, (500,580))
                    pygame.mixer.music.play(0)
                    pygame.display.update()

                    pygame.draw.rect(gameDisplay, BLACK, (478, 387, 110, 50), 0)
                    pygame.draw.rect(gameDisplay, BLACK, (478, 487, 110, 50), 0)
                    pygame.draw.rect(gameDisplay, BLACK, (478, 587, 110, 50), 0)

                    save_pause = True

                    while save_pause:
                        for event in pygame.event.get():
                            mouse = pygame.mouse.get_pos()
                            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                                if 430 + 300 > mouse[0] > 430 and 870 + 80 > mouse[1] > 870: #GO BACK HOME
                                    pygame.mixer.music.play(0)
                                    home = True
                                    save_pause = False
                                    pause = False
                                if 478 + 110 > mouse[0] > 478 and 387 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.play(0)
                                    save_game(file_path1, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run)
                                    break
                                elif 478 + 110 > mouse[0] > 478 and 487 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.play(0)
                                    save_game(file_path2, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run)
                                    break
                                elif 478 + 110 > mouse[0] > 478 and 587 + 50 > mouse[1] > 387: #START GAME
                                    pygame.mixer.music.play(0)
                                    save_game(file_path3, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run)
                                    break
                            if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                                save_pause = False
                
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                pause = False

    return home

def save_game(file_path, snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run):
    pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake pause.wav')
    pygame.mixer.music.play(0)
    with open(file_path, "wb") as file:
        data = (snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run)
        pickle.dump(data, file)

def load_game(file_path):
    with open(file_path, "rb") as file:
        # Load the binary file and restore the grid, score, and food_location variables
        snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run = pickle.load(file)
    return snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run

# def save_screen():


def create_button(x, y, width, height, text):

    # Create a font object
    font = pygame.font.Font(FONT, 35)
    # Render the text to a surface
    text_surface = font.render(text, True, (255, 255, 255))
    gameDisplay.blit(text_surface, (x + width / 2 - text_surface.get_width() / 2, y + height / 2 - text_surface.get_height() / 2))

    # THIS WAS JUST MEANT TO BE USED TO SHOW CLICKABLE BOUNDS
    # pygame.draw.rect(gameDisplay, WHITE, (x, y1, width, height), 0)
    # pygame.draw.rect(gameDisplay, WHITE, (x, y2, width, height), 0)
    # pygame.draw.rect(gameDisplay, WHITE, (x, y3, width, height), 0)

def draw_buttons():
    if snake.score < 20:
        create_button(x, y1, 300, 60, '-3 Links')
        create_button(x, y2, 300, 60, '-5 Speed')
    elif snake.score >= 15:
        create_button(x, y1, 300, 60, '-3 Links')
        create_button(x, y2, 300, 60, '-5 Speed')
        create_button(x, y3, 300, 60, '2x Multiplier')


def button_screen():
    pause_background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/pause screen.png')
    sub_screen = pygame.Surface((395, 395))
    sub_screen.fill(BLACK)
    gameDisplay.blit(sub_screen, [310, 310])
    gameDisplay.blit(pause_background, [0, -35])

    # Create new buttons
    draw_buttons()
    pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop food.wav')
            pygame.mixer.music.play(0)
            mouse = pygame.mouse.get_pos()
            if x + 300 > mouse[0] > x and y1 + 60 > mouse[1] > y1:
                remove_parts()
                return
            if x + 300 > mouse[0] > x and y2 + 60 > mouse[1] > y2:
                slow_snake()
                return
            if snake.score >= 15:
                if x + 300 > mouse[0] > x and y3 + 60 > mouse[1] > y3:
                    multiply_score()
                    return

            


def remove_parts():
    snake_body = len(snake.body)
    while len(snake.body) >= snake_body - 2:
        snake.body = snake.body[:-1]

def slow_snake():
    global framerate
    framerate = framerate - 5

def multiply_score():
    global multiplier
    multiplier = multiplier * 2

class Snake:
    def __init__(self):
        self.body = [(9, 6), (9, 7), (9, 8)]
        self.direction = "UP"
        self.score = 0
        self.tokens = 0

    def change_direction(self, direction):
        if direction == "UP" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "DOWN" and self.direction != "LEFT":
            self.direction = "RIGHT" 
        elif direction == "LEFT" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "RIGHT" and self.direction != "UP":
            self.direction = "DOWN"

    def move(self):

        x, y = self.body[0]

        if self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "RIGHT":
            x += 1

        self.body.insert(0, (x, y))

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
        if homescreen:
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

pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop.wav')

first_key_pressed = False

elapsed_time = 0
framerate = 20
multiplier = 1
food_counter = 0
body_count = 0
snake = Snake()
food_pos = (random.randint(0, 19), random.randint(0, 19))
token_pos = (random.randint(0, 19), random.randint(0, 19))

# Define font
font = pygame.font.Font(FONT, 45)        
font2 = pygame.font.Font(FONT, 150)
font3 = pygame.font.Font(FONT, 25)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
if_statement_run = False
sound_played = False
while not done:
    
    #GOLD FOOD BLOCK
    if not if_statement_run and snake.score % 10 == 1 and snake.score != 1:
        if not sound_played:
            pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake pause.wav')
            pygame.mixer.music.play(0)
            button_screen()
            sound_played = True
        framerate = framerate + 5
        if_statement_run = True
        first_key_pressed = False

        #TESTING FRAMERATE FUNCTION
        # print(framerate)



    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if not first_key_pressed:
                pygame.mixer.music.play(-1)
                first_key_pressed = True
            if event.key == pygame.K_TAB:
                home = pause_screen()
                if home:
                    homescreen = True
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")



        elif if_statement_run and snake.score % 10 == 0:
            if_statement_run = False
            sound_played = False

    # --- Game logic should go here

    if first_key_pressed:
        snake.move()
        elapsed_time += clock.tick(framerate) / 1000.0
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop.wav')
        pygame.mixer.music.play(-1)

    if snake.check_collision():
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake collision.wav')
        pygame.mixer.music.play(0)
        framerate = 20
        elapsed_time = 0
        multiplier = 1
        food_pos = (random.randint(0, 19), random.randint(0, 19))
        first_key_pressed = False
        food_counter = 0
        body_count = 0
        snake = Snake()

    if snake.score < 20:
        x = 350
        y1 = 400
        y2 = 470
    elif snake.score >= 15:
        y1 = 370
        y2 = 440
        y3 = 510    

    quicker = snake.score % 10 == 0 and snake.score != 0

    if snake.check_food():
        food_counter += multiplier
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/snake loop food.wav')
        pygame.mixer.music.play(0)
        while (snake.score % 3 != 0 or snake.score == 0):
            food_pos = (random.randint(0, 19), random.randint(0, 19))
            if food_pos not in snake.body:
                break

    if snake.check_token():
        food_counter += 1
        pygame.mixer.music.load('/Users/apple/Snake-Game/Snake/Assets/token.wav')
        pygame.mixer.music.play(0)
        print(snake.score)
        while snake.score % 3 == 1 and snake.score != 0:
            token_pos = (random.randint(0, 19), random.randint(0, 19))
            if token_pos not in snake.body and token_pos != food_pos:
                break

    

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    if homescreen:
        file = home_screen()

    
    if game_loaded:
        snake, framerate, multiplier, food_counter, score, elapsed_time, food_pos, token_pos, body_count, if_statement_run = load_game(file)
        game_loaded = False

    # Draw the grid
    for row in range(20):
        for column in range(20):
            color = WHITE
            if (row, column) in snake.body:
                color = GREEN
            elif (snake.score % 3 != 0 or snake.score == 0) and (row, column) == food_pos:
                color = RED
            elif snake.score % 3 == 0 and snake.score != 0 and (row, column) == token_pos:
                color = GOLD
            pygame.draw.rect(
                screen,
                color,
                [
                    (MARGIN + WIDTH) * column + MARGIN + 175,
                    (MARGIN + HEIGHT) * row + MARGIN + 175,
                    WIDTH,
                    HEIGHT,
                ],
            )    
            

    # Get score
    score = food_counter

    background = pygame.image.load('/Users/apple/Snake-Game/Snake/Assets/Snake Trees.png')
    score_text = font.render("Score: " + str(score), True, WHITE)
    time_text = font.render("{:02d}:{:02d}".format(int(elapsed_time // 60), int(elapsed_time % 60)), True, WHITE)
    game_text = font2.render("SNAKE", True, WHITE)
    token_text = font3.render("Tokens:" + str(snake.tokens), True, WHITE)

    with open(file_path1, "rb") as file:
        data = pickle.load(file)
    save_file1_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
    save_file1_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))

    with open(file_path2, "rb") as file:
        data = pickle.load(file)
    save_file2_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
    save_file2_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))

    with open(file_path3, "rb") as file:
        data = pickle.load(file)
    save_file3_tokens = font3.render(f'tokens: {data[0].tokens}', True, (255, 255, 255)) 
    save_file3_score = font3.render(f'score: {data[3]}', True, (255, 255, 255))

    # Display score and time
    gameDisplay.blit(score_text, [50, 65])
    gameDisplay.blit(token_text, [50, 125])
    gameDisplay.blit(time_text, [875, 70])
    gameDisplay.blit(game_text, [320, 25])
    gameDisplay.blit(background, [0,-25])

    pygame.display.update()

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(framerate)