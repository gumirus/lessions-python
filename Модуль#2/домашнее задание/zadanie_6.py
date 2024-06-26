'''
Цель: создать игровое приложение с использованием 
языка программирования Python и библиотеки Pygame, 
которые обеспечивают возможности разработки игр на 
основе объектно-ориентированных принципов, поддержку 
изображений, анимации, управление основным 
игровым объектом (Персонажем).

    Что нужно сделать:
1. Создать игровое поле
2. Создать игровой объект “Змейка”
3. Создать игровой объект “Яблоко”
4. Реализовать алгоритм добавления
   блоков к змейке в случае поедания
   яблока
'''

import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
FRAME_COLOR = (0, 255, 204)
RECT_COLOR = (255, 255, 255)
OTHER_RECT_COLOR = (204, 255, 255)
HEADER_COLOR = (0, 170, 150)

# Определение скорости
clock = pygame.time.Clock()
snake_speed = 15

# Размеры блока змейки и яблока
block_size = 20

# Класс Змейка
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])  
        self.color = green
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*block_size)) % width), (cur[1] + (y*block_size)) % height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], block_size, block_size))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))  
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))  
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))

# Класс Яблоко
class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (width // block_size) - 1) * block_size,
                         random.randint(0, (height // block_size) - 1) * block_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], block_size, block_size))

def draw_grid():
    for row in range(0, height, block_size):
        for col in range(0, width, block_size):
            if (row // block_size + col // block_size) % 2 == 0:
                color = RECT_COLOR
            else:
                color = OTHER_RECT_COLOR
            pygame.draw.rect(win, color, pygame.Rect(col, row, block_size, block_size))

def main():
    snake = Snake()
    apple = Apple()

    while True:
        snake.handle_keys()
        snake.move()
        if snake.get_head_position() == apple.position:
            snake.length += 1
            snake.score += 1
            apple.randomize_position()

        win.fill(FRAME_COLOR)
        draw_grid()
        snake.draw(win)
        apple.draw(win)

        # Отображение текущего счёта
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {snake.score}", True, black)
        win.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(snake_speed)

if __name__ == "__main__":
    main()
