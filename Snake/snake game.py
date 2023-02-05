import pygame
import random

elapsed_time = 0
FONT = "/Users/apple/Desktop/Snake/8Bit.ttf"

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215,0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
MARGIN = 3

def create_button(x, y, width, height, inactive_color, active_color, text, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Create a font object
    font = pygame.font.Font(FONT, 22)
    # Render the text to a surface
    text_surface = font.render(text, True, (255, 255, 255))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    gameDisplay.blit(text_surface, (x + width / 2 - text_surface.get_width() / 2, y + height / 2 - text_surface.get_height() / 2))

def draw_buttons():
    create_button(350, 350, 300, 60, BLACK, (0, 255, 0), 'Remove 5 links from snake', remove_parts)
    create_button(350, 420, 300, 60, BLACK, (0, 255, 0), 'Keep snake same speed', lower_speed)


def button_screen():
    sub_screen = pygame.Surface((395, 395))
    sub_screen.fill(BLACK)
    gameDisplay.blit(sub_screen, [310, 310])

    # Create new buttons
    draw_buttons()

    pygame.display.update()
    pause = True
    while pause:
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
                    pause = False


def remove_parts():
    snake_body = len(snake.body)
    while len(snake.body) >= snake_body - 2:
        snake.body = snake.body[:-1]

def lower_speed():
    framerate = framerate - 5



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

framerate = 20

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

first_key_pressed = False

# -------- Main Program Loop -----------
if_statement_run = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if not first_key_pressed:
                first_key_pressed = True
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

        if not if_statement_run and food_counter % 10 == 1 and food_counter != 1:
            if_statement_run = True
            framerate = 25
            button_screen()
        elif if_statement_run and food_counter % 10 == 0:
            if_statement_run = False

    # --- Game logic should go here

    if first_key_pressed:
        snake.move()
        elapsed_time += clock.tick(framerate) / 1000.0

    if snake.check_collision():
        framerate = 20
        elapsed_time = 0
        food_pos = (random.randint(0, 19), random.randint(0, 19))
        first_key_pressed = False
        food_counter = 0
        body_count = 0
        snake = Snake()

    quicker = food_counter % 10 == 0 and food_counter != 0

    if quicker:
        food_color = GOLD
    else:
        food_color = RED

    if snake.check_food():
        food_counter += 1
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
    backgrounds = ['/Users/apple/Desktop/Snake/Background BW.png',]

    background = pygame.image.load('/Users/apple/Desktop/Snake/Background BW.png')
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