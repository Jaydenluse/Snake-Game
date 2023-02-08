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