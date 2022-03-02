import pygame
from snake import*

pygame.init()
bounds = (600,600)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
block_size = 20
snake = snake (block_size)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.move()
    window.fill((0,0,0))
    snake.draw(pygame, window)
    pygame.display.update()