import pygame

pygame.init()

# Constants
HEIGHT = 600
FRAME_COLOR = (0, 255, 204)
RECT_COLOR = (255, 255, 255)
SIZE_RECT = 20
COUNT_RECTS = 20
OTHER_RECT_COLOR = (204, 255, 255)
RETURN = 1
WIDTH = SIZE_RECT * COUNT_RECTS + 2 * SIZE_RECT + RETURN * SIZE_RECT
HEADER_RECT = 70
HEADER_COLOR = (0, 170, 150)
COLOR_SNAKE = (255, 0, 0)  # Example snake color

# Initialize the game window
app = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')

# Function to draw a rectangle on the grid
def draw_rect(color, row, column):
    pygame.draw.rect(app, color, [SIZE_RECT + column * SIZE_RECT + RETURN * (column + 1),
                                  HEADER_RECT + row * SIZE_RECT + RETURN * (row + 1),
                                  SIZE_RECT, SIZE_RECT])

# Initial snake position
snake_rect = [(10, 10), (10, 11), (10, 12)]

# Snake direction
direction = pygame.K_RIGHT

# Clock object to control the frame rate
clock = pygame.time.Clock()

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                direction = event.key

    if direction == pygame.K_UP:
        x_row, y_col = -1, 0
    elif direction == pygame.K_DOWN:
        x_row, y_col = 1, 0
    elif direction == pygame.K_LEFT:
        x_row, y_col = 0, -1
    elif direction == pygame.K_RIGHT:
        x_row, y_col = 0, 1

    # Move the snake
    new_head = (snake_rect[0][0] + x_row, snake_rect[0][1] + y_col)
    snake_rect = [new_head] + snake_rect[:-1]

    app.fill(FRAME_COLOR)
    pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIDTH, HEADER_RECT])

    for row in range(COUNT_RECTS):
        for column in range(COUNT_RECTS):
            if (row + column) % 2 == 0:
                color = RECT_COLOR
            else:
                color = OTHER_RECT_COLOR
            draw_rect(color, row, column)

    for x, y in snake_rect:
        draw_rect(COLOR_SNAKE, x, y)
        
    pygame.display.update()
    clock.tick(10)

pygame.quit()
