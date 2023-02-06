import pygame
import random
import pickle # Will use to save later

framerate = 20
multiplier = 1
elapsed_time = 0
FONT = "/Users/apple/Desktop/Snake/Snake-Game/Snake/8Bit.ttf"
pygame.mixer.init()

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

def pause_screen():

    pygame.mixer.music.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/snake pause.wav')
    pygame.mixer.music.play(0)

    pause_background = pygame.image.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/pause screen.png')
    sub_screen = pygame.Surface((395, 395))
    sub_screen.fill(BLACK)
    gameDisplay.blit(sub_screen, [310, 310])
    gameDisplay.blit(pause_background, [0, -35])

    font = pygame.font.Font(FONT, 35)
    speed = font.render(f'Speed:     {framerate}', True, (255, 255, 255))
    links = font.render(f'Links:     {len(snake.body)}', True, (255, 255, 255))
    multiplier_text = font.render(f'Multiplier:     {multiplier} x', True, (255, 255, 255))
    gameDisplay.blit(speed, (430,375))
    gameDisplay.blit(links, (440,450))
    gameDisplay.blit(multiplier_text, (410,525))
    pygame.display.update()

    pause = True

    while pause:
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP and event.button == 1 or event.type == pygame.KEYDOWN and event.key == pygame.K_TAB):
                pause = False

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
    pause_background = pygame.image.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/pause screen.png')
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

        return False
        

    def check_food(self):
        # Check if the snake ate the food
        if self.body[0] == food_pos:
            self.score += 1
            return True

        return False

# Initialize pygame
pygame.init()

pygame.mixer.music.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/snake loop.wav')

first_key_pressed = False

elapsed_time = 0

# Set display dimensions
display_width = 600
display_height = 600

# Initialize game display
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Define colors
black = (0,0,0)
white = (255,255,255)

# Define font
font = pygame.font.Font(FONT, 45)        
font2 = pygame.font.Font(FONT, 150)

food_counter = 0
body_count = 0

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snake = Snake()

# Generate the initial food position
food_pos = (random.randint(0, 19), random.randint(0, 19))

# -------- Main Program Loop -----------
if_statement_run = False
sound_played = False
while not done:

    #GOLD FOOD BLOCK
    if not if_statement_run and snake.score % 10 == 1 and snake.score != 1:
        if not sound_played:
            pygame.mixer.music.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/snake pause.wav')
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
                pause_screen()
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
        pygame.mixer.music.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/snake loop.wav')
        pygame.mixer.music.play(-1)

    if snake.check_collision():
        pygame.mixer.music.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/snake collision.wav')
        pygame.mixer.music.play(0)
        framerate = 20
        elapsed_time = 0
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
        pygame.mixer.music.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/snake loop food.wav')
        pygame.mixer.music.play(0)
        while True:
            food_pos = (random.randint(0, 19), random.randint(0, 19))
            if food_pos not in snake.body:
                break

    

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # Draw the grid
    for row in range(20):
        for column in range(20):
            color = WHITE
            if (row, column) in snake.body:
                color = GREEN
            elif (row, column) == food_pos:
                if quicker:
                    food_color = GOLD
                else:
                    food_color = RED
                color = food_color
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

    #Background list
    backgrounds = ['/Users/apple/Desktop/Snake/Snake-Game/Snake/Background BW.png']

    background = pygame.image.load('/Users/apple/Desktop/Snake/Snake-Game/Snake/Snake Background.png')
    score_text = font.render("Score: " + str(score), True, white)
    time_text = font.render("{:02d}:{:02d}".format(int(elapsed_time // 60), int(elapsed_time % 60)), True, white)
    game_text = font2.render("SNAKE", True, white)

    # Display score and time
    gameDisplay.blit(score_text, [50, 65])
    gameDisplay.blit(time_text, [875, 70])
    gameDisplay.blit(game_text, [320, 25])
    gameDisplay.blit(background, [0,-25])

    pygame.display.update()

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(framerate)