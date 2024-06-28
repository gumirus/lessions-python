import pygame
import random

pygame.init()

#WIDTH = 500
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
COLOR_SNAKE = (0, 102, 0)
FOOD_COLOR = (255, 0, 0)


app = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')

game_over = True
is_game_started = False

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def inside(self):
        return 0 <= self.x < COUNT_RECTS and  0 <= self.y < COUNT_RECTS
    
    def __eq__(self, other):
        return isinstance(other, Snake) and self.x == other.x and self.y == other.y

def draw_rect(color, row, column):
    pygame.draw.rect(app, color, [SIZE_RECT + column * SIZE_RECT + RETURN * (column + 1),
                                              HEADER_RECT + row * SIZE_RECT + RETURN * (row + 1),
                                              SIZE_RECT, SIZE_RECT])
def random_food_block():
    x = random.randint(0, COUNT_RECTS - 1)
    y = random.randint(0, COUNT_RECTS - 1)

    food_block = Snake(x, y)
    while food_block in snake_rect:
       food.x = random.randint(0, COUNT_RECTS - 1)
       food.y = random.randint(0, COUNT_RECTS - 1) 
    return food_block

x_row = 0
y_col = 1
result = 0
snake_rect = [Snake(1, 2)]
time = pygame.time.Clock()
food = random_food_block()
text = pygame.font.SysFont('courier', 36)
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        elif event.type == pygame.KEYDOWN:
            if not is_game_started:
                is_game_started = True
            elif event.key == pygame.K_UP and y_col != 0:
                x_row = -1
                y_col = 0
            elif event.key == pygame.K_DOWN and y_col != 0:
                x_row = 1
                y_col = 0
            elif event.key == pygame.K_RIGHT and x_row != 0:
                x_row = 0
                y_col = 1
            elif event.key == pygame.K_LEFT and x_row != 0:
                x_row = 0
                y_col = -1
            
            
    app.fill(FRAME_COLOR)

    if not is_game_started:
        text_menu = text.render('For start press any key', 4, RECT_COLOR)
        app.blit(text_menu, (SIZE_RECT, HEIGHT // 2))
    else:
        pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIDTH, HEADER_RECT])

        for row in range(COUNT_RECTS):
            for column in range(COUNT_RECTS):
                if (row + column) % 2 == 0:
                    color = RECT_COLOR
                else:
                    color = OTHER_RECT_COLOR

                draw_rect(color, row, column)

        draw_rect(FOOD_COLOR, food.x, food.y)

        for rect in snake_rect:
            draw_rect(COLOR_SNAKE, rect.x, rect.y)

        head = snake_rect[-1]

        if food == head:
            result += 1
            snake_rect.append(food)
            food = random_food_block()

        if not head.inside():
            game_over = False

        new_head = Snake(head.x + x_row, head.y + y_col)
        snake_rect.append(new_head)
        snake_rect.pop(0)

        text_result = text.render(f'Score: {result}', 0, RECT_COLOR)
        app.blit(text_result, (SIZE_RECT, SIZE_RECT))

    pygame.display.update()
    time.tick(10)

pygame.quit()