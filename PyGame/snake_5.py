import pygame
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")

game_over = False

snake_block = 10
snake_speed = 15

snake_List = []
Length_of_snake = 1

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

x1 = 300
y1 = 400

x1_change = 0
y1_change = 0

z1 = random.randrange(10, 490, 10)
z2 = random.randrange(10, 490, 10)

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    if x1 == z1 and y1 == z2:
        Length_of_snake += 1
        z1 = random.randrange(10, 490, 10)
        z2 = random.randrange(10, 490, 10)

    if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    our_snake(snake_block, snake_List)

    pygame.draw.rect(dis, red, [z1, z2, 10, 10])
    pygame.display.update()

    clock.tick(15)

pygame = quit()
quit()
