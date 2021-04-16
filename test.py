import pygame, sys
from pygame.locals import *
pygame.init()
WIDTH = 400
HEIGHT = 300
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Moving square")

screen.fill(Color("blue"))
FPS = 300
clock = pygame.time.Clock()

CAR_SIZE = 20
CAR_STEP = 1
car_x = (WIDTH-CAR_SIZE)/2
car_y = HEIGHT-CAR_SIZE



left_arrow = False
right_arrow = False
up_arrow = False
down_arrow = False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right_arrow = True
            elif event.key == K_LEFT:
                left_arrow = True
            elif event.key == K_UP:
                up_arrow = True
            elif event.key == K_DOWN:
                down_arrow = True

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                right_arrow = False
            elif event.key == K_LEFT:
                left_arrow = False
            elif event.key == K_UP:
                up_arrow = False
            elif event.key == K_DOWN:
                down_arrow = False

    screen.fill(Color("blue"))
    if right_arrow:
        car_x = min(car_x + CAR_STEP, WIDTH-CAR_SIZE)
    if left_arrow:
        car_x = max(car_x - CAR_STEP, 0)
    if up_arrow:
        car_y = max(car_y - CAR_STEP, 0)
    if down_arrow:
        car_y = min(car_y + CAR_STEP, HEIGHT-CAR_SIZE)

    pygame.draw.rect(screen, Color("red"), (car_x, car_y, CAR_SIZE, CAR_SIZE) )
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
