# крестики нолики
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)

WIDTH, HEIGHT = 300, 400
LINE_WIDTH = 15
CELL_SIZE = WIDTH // 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики нолики')

font = pygame.font.SysFont(None, 40)
button_font = pygame.font.SysFont(None, 30)

score_X = 0
score_O = 0

def draw_grid():
    screen.fill(WHITE)
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), 
                         (x * CELL_SIZE, HEIGHT - 100), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), 
                         (WIDTH, x * CELL_SIZE), LINE_WIDTH)

def draw_figures(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col *
                CELL_SIZE + CELL_SIZE // 5, row *
                CELL_SIZE + CELL_SIZE // 5), (col *
                CELL_SIZE + 4 * CELL_SIZE // 5, row *
                CELL_SIZE + 4 * CELL_SIZE // 5), LINE_WIDTH)

                pygame.draw.line(screen, RED, (col *
                CELL_SIZE + 4 * CELL_SIZE // 5, row *
                CELL_SIZE + CELL_SIZE // 5), (col *
                CELL_SIZE + CELL_SIZE // 5, row *
                CELL_SIZE + 4 * CELL_SIZE // 5), LINE_WIDTH)

            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col *
                CELL_SIZE + CELL_SIZE // 2, row *
                CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 3, LINE_WIDTH)

def draw_score():
    score_text = f"X: {score_X} - O: {score_O}"
    score_surface = font.render(score_text, True, BLACK)
    screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, HEIGHT - 90))

def draw_button():
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 60, 200, 50)
    pygame.draw.rect(screen, GREY, button_rect)
    button_text = 'Начать новую игру'
    button_surface = button_font.render(button_text, True, BLACK)
    screen.blit(button_surface, (WIDTH // 2 - button_surface.get_width() // 2, HEIGHT - 50))
    return button_rect

def check_winner(board):
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]
            and board[row][0] is not None):
            return board[row][0]
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]
            and board[0][col] is not None):
            return board[0][col]
    if (board[0][0] == board[1][1] == board[2][2]
            and board[0][0] is not None):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]
            and board[0][2] is not None):
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if None in row:
            return False
    return True

def reset_board():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]

board = reset_board()
player = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (game_over and HEIGHT - 60 <= mouseY <= HEIGHT - 10 and 
                WIDTH // 2 - 100 <= mouseX <= WIDTH // 2 + 100):
                board = reset_board()
                game_over = False 
                player = 'X'
            elif not game_over and mouseY < HEIGHT - 100: 
                clicked_row = mouseY // CELL_SIZE 
                clicked_col = mouseX // CELL_SIZE
                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player 
                    player = 'O' if player == 'X' else 'X'

    winner = check_winner(board)
    if winner is not None:
        if not game_over: 
            if winner == 'X':
                score_X += 1
            else:
                score_O += 1
            game_over = True

    if check_draw(board) and winner is None:
        game_over = True

    draw_grid()
    draw_figures(board)
    draw_score()
    button_rect = draw_button()
    pygame.display.flip()
