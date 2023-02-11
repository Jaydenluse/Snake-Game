from constants import UP, RIGHT, DOWN, LEFT

class Snake:
    def __init__(self):
        self.body = [(9, 6), (9, 7), (9, 8)]
        self.direction = UP

    def change_direction(self, direction):
        if direction == UP and self.direction != DOWN:
            self.direction = LEFT
        elif direction == DOWN and self.direction != UP:
            self.direction = RIGHT 
        elif direction == LEFT and self.direction != RIGHT:
            self.direction = UP
        elif direction == RIGHT and self.direction != DOWN:
            self.direction = DOWN

    def move(self):
        y, x = self.body[0]

        if self.direction == UP:
            y -= 1
        elif self.direction == DOWN:
            y += 1
        elif self.direction == LEFT:
            x -= 1
        elif self.direction == RIGHT:
            x += 1

        self.body.insert(0, (y, x))

        self.last_pos = self.body.pop()

    def grow(self) -> None:
        self.body.append(self.last_pos)
