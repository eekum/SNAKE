import pygame
from food import Food
from snake import*

pygame.init()
bounds = (600,600)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")
block_size = 20
snake = snake (block_size, bounds)
food = Food(block_size,bounds)
font = pygame.font.SysFont('comicsans' ,60, True)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    snake.steer(Direction.left)
elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.right)
elif keys[pygame.K_UP]:
    snake.steer(Direction.up)
elif keys[pygame.K_DOWN]:
    snake.steer(Direction.down)

    snake.move()
    snake.check_for_food(food)
    if snake.check_bounds() == True or snake.check_tail_collision() == True:
       text = font.render('Game Over', True, (255,255,255))
       window.blit(text, (20,120))
       pygame.display.update()
       pygame.time.delay(1000)
       snake.respawn()
       food.respawn()    
    window.fill((0,0,0))
    snake.draw(pygame, window)
    food.draw(pygame, window)
    pygame.display.update()