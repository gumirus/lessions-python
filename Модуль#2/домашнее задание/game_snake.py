import pygame
import random

pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 102, 0)
GREEN_LIGHT = (0, 170, 150)
FRAME_COLOR = (0, 255, 204)
RECT_COLOR = (255, 255, 255)
OTHER_RECT_COLOR = (205, 255, 255)

# Скорость змейки
clock = pygame.time.Clock()
snake_speed = 5

# Размер змейки и яблока
block_size = 25

# Класс Змейка
class Snake:
  def __init__(self):
    self.length = 1
    self.positions = [((WIDTH // 2), (HEIGHT // 2))]
    self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    self.color = GREEN
    self.score = 0

  def get_head_position(self):
    return self.positions[0]

  def turn(self, point):
    if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
      return
    else:
      self.direction = point

  def move(self):
    cur = self.get_head_position()
    x, y = self.direction
    new = (cur[0] + (x * block_size), cur[1] + (y * block_size))
    if (new[0] < block_size or new[0] >= WIDTH - block_size or
        new[1] < block_size * 3 or new[1] >= HEIGHT - block_size):
      return True
    if new in self.positions[1:]:
      return True
    self.positions.insert(0, new)
    if len(self.positions) > self.length:
      self.positions.pop()
    return False

  def reset(self):
    self.length = 1
    self.positions = [((WIDTH // 2), (HEIGHT // 2))]
    self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
    self.score = 0

  def draw(self, surface):
    for p in self.positions:
      pygame.draw.rect(surface, self.color, (p[0], p[1], block_size - 2, block_size - 2))

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

  def update_high_score(self, current_high_score):
    if self.score > current_high_score:
      return self.score
    else:
      return current_high_score

# Класс Яблоко
class Apple:
  def __init__(self, snake):
    self.position = (0, 0)
    self.color = RED
    self.snake = snake
    self.randomize_position()

  def randomize_position(self):
    while True:
      x = random.randint(1, (WIDTH // block_size) - 2) * block_size
      y = random.randint(3, (HEIGHT // block_size) - 2) * block_size
      if (x, y) != self.snake.get_head_position() and (x, y) not in self.snake.positions and y >= block_size * 3:
        break
    self.position = (x, y)

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], block_size - 2, block_size - 2))


def draw_grid(surface):
  for row in range(0, HEIGHT, block_size):
    for col in range(0, WIDTH, block_size):
      if (row // block_size + col // block_size) % 2 == 0:
        color = RECT_COLOR
      else:
        color = OTHER_RECT_COLOR
      pygame.draw.rect(surface, color, pygame.Rect(col, row, block_size, block_size))

def draw_borders(surface):
  pygame.draw.rect(surface, GREEN_LIGHT, pygame.Rect(0, HEIGHT - block_size, WIDTH, block_size))
  pygame.draw.rect(surface, GREEN_LIGHT, pygame.Rect(0, 0, block_size, HEIGHT))
  pygame.draw.rect(surface, GREEN_LIGHT, pygame.Rect(WIDTH - block_size, 0, block_size, HEIGHT))

def draw_header(surface, score, high_score):
  pygame.draw.rect(surface, GREEN_LIGHT, pygame.Rect(0, 0, WIDTH, block_size * 3))
  font = pygame.font.SysFont("Arial", 24)
  score_text = font.render(f"Счёт: {score}", True, BLACK)
  high_score_text = font.render(f"Рекорд: {high_score}", True, BLACK)
  surface.blit(score_text, (block_size, block_size))
  surface.blit(high_score_text, (WIDTH - block_size - high_score_text.get_width(), block_size))

def main():
  snake = Snake()
  apple = Apple(snake)
  start_game = False
  game_over = False
  high_score = 0

  while True:
    pygame.display.update()
    if not start_game:
      win.fill(FRAME_COLOR)
      font = pygame.font.SysFont("Arial", 36)
      text = font.render("Нажмите любую клавишу", True, BLACK)
      win.blit(text, (WIDTH // 4, HEIGHT // 2))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif event.type == pygame.KEYDOWN:
          start_game = True
          game_over = False
          snake.reset()
    elif game_over:
      win.fill(FRAME_COLOR)
      font = pygame.font.SysFont("Arial", 36)
      text = font.render("Игра окончена.", True, RED)
      win.blit(text, (WIDTH // 8, HEIGHT // 2))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        elif event.type == pygame.KEYDOWN:
          start_game = False
          game_over = False
    else:
      snake.handle_keys()
      game_over = snake.move()
      if snake.get_head_position() == apple.position:
        snake.length += 1
        snake.score += 1
        apple.randomize_position()
        high_score = snake.update_high_score(high_score)

      win.fill(FRAME_COLOR)
      draw_grid(win)
      draw_borders(win)
      draw_header(win, snake.score, high_score)
      snake.draw(win)
      apple.draw(win)

    clock.tick(snake_speed)

if __name__ == "__main__":
  main()
