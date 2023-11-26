import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
SNAKE_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.grid_size = GRID_SIZE
        self.snake_size = SNAKE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = RIGHT
        self.food = self.generate_food()

    def generate_food(self):
        while True:
            food = (random.randint(0, (self.width - self.grid_size) // self.grid_size) * self.grid_size,
                    random.randint(0, (self.height - self.grid_size) // self.grid_size) * self.grid_size)
            if food not in self.snake:
                return food

    def draw_grid(self):
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, self.height))
        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(self.screen, WHITE, (0, y), (self.width, y))

    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, WHITE, (segment[0], segment[1], self.snake_size, self.snake_size))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], self.snake_size, self.snake_size))

    def move_snake(self):
        head = (self.snake[0][0] + self.direction[0] * self.grid_size,
                self.snake[0][1] + self.direction[1] * self.grid_size)
        self.snake.insert(0, head)

        # Check if the snake eats the food
        if head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        # Check if the snake hits the wall or itself
        if (
            head[0] < 0 or head[0] >= self.width or
            head[1] < 0 or head[1] >= self.height or
            head in self.snake[1:]
        ):
            return True
        return False

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            self.move_snake()

            if self.check_collision():
                print("Game Over!")
                pygame.quit()
                sys.exit()

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_snake()
            self.draw_food()

            pygame.display.flip()
            clock.tick(10)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
