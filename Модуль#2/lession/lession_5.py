# import pygame
# import sys

# #Константы

# WIDTH = 360
# HEIGHT = 480
# FPS = 30

# white = (255, 255, 255)

# init = pygame.init()

# if init == (5, 0):
#   pass
# else:
#   pygame.quit()
#   sys.exit()


# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('My Game')
# clock = pygame.time.Clock()

# #Функции

# def game():
#   pass

# running = True
# while running:
#   clock.tick(FPS)
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False
# pygame.quit()
# sys.exit()

#--------------------------------------------------------------

# import pygame
# import sys

# pygame.init()

# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Simple Test Game')

# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)

# player_size = 50
# player_pos = [screen_width // 2, screen_height // 2]
# player_speed = 10

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player_pos[0] -= player_speed
#     if keys[pygame.K_RIGHT]:
#         player_pos[0] += player_speed
#     if keys[pygame.K_RIGHT]:
#         player_pos[0] += player_speed
#     if keys[pygame.K_UP]:
#         player_pos[1] -= player_speed
#     if keys[pygame.K_DOWN]:
#         player_pos[1] += player_speed

# player_pos[0]= max(0, min(player_pos[0], screen_width - player_size))
# player_pos[1] = max(0, min(player_pos[1], screen_height - player_size))
# screen.fill(white)
# pygame.draw.rect(screen, red, (player_pos[0], player_pos[1],player_size, player_size))
# pygame.display.flip()
# pygame.time.Clock().tick(30)

#-------------------------------------------------------------------------------------------

import pygame
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dodge Game with Multiple Enemies!')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

player_size = 50
player_pos =[screen_width // 2, screen_height - 2 * player_size]
player_speed = 10

enemy_size = 50
enemy_list = []
enemy_speed = 10
num_enemies = 5

def create_enemies(enemy_list, num_enemies):
    for _ in range(num_enemies):
        x_pos = random.randint(0, screen_width - enemy_size)
        y_pos = random.randint(-screen_height, 0)
        enemy_list.append([x_pos, y_pos])

def update_enemy_positions(enemy_list):
    for enemy_pos in enemy_list:
        enemy_pos[1] += enemy_speed
        if enemy_pos[1] > screen_height:
            enemy_list.remove(enemy_pos)
            new_enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
            enemy_list.append(new_enemy_pos)

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos [1]

    e_x = enemy_pos[0]
    e_y = enemy_pos [1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y+ player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

running = True
clock = pygame.time.Clock()

create_enemies(enemy_list, num_enemies)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed

    player_pos[0]= max(0, min(player_pos[0], screen_width - player_size))

    update_enemy_positions(enemy_list)

    for enemy_pos in enemy_list:
        if detect_collision(player_pos, enemy_pos):
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, blue, (player_pos[0],player_pos[1], player_size, player_size))

    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, red, (enemy_pos[0],enemy_pos[1], enemy_size, enemy_size))

    pygame.display.flip()
    clock.tick(30)

print("Game Over!")


