import pygame
import random

start_time = pygame.time.get_ticks()

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

# Set display dimensions
display_width = 600
display_height = 600

# Initialize game display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game Display')

# Define colors
black = (0,0,0)
white = (255,255,255)

# Define font
font = pygame.font.Font("/Users/apple/Desktop/Snake/8Bit.ttf", 45)
font2 = pygame.font.Font("/Users/apple/Desktop/Snake/8Bit.ttf", 150)

food_counter = 0
body_count = 0

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1000, 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Snake")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snake = Snake()

# Generate the initial food position
food_pos = (random.randint(0, 19), random.randint(0, 19))

first_key_pressed = False

# -------- Main Program Loop -----------
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

    # --- Game logic should go here

    if first_key_pressed:
        snake.move()

    if snake.check_collision():
        done = True

    if food_counter % 10 == 0 and food_counter != 0:
        food_color = GOLD
    elif food_counter % 10 == 1 and food_counter != 1:
        food_color = RED
        while len(snake.body) >= (food_counter/2):
            snake.body = snake.body[:-1]
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

    # Get time elapsed
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    # Get score
    score = food_counter

    score_text = font.render("Score: " + str(score), True, white)
    time_text = font.render("{:02d}:{:02d}".format(int(elapsed_time // 60), int(elapsed_time % 60)), True, white)
    game_text = font2.render("SNAKE", True, white)

    # Display score and time
    gameDisplay.blit(score_text, [50, 65])
    gameDisplay.blit(time_text, [875, 70])
    gameDisplay.blit(game_text, [320, 25])

    pygame.display.update()

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)