# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
# When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key.
# The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored

import pygame
import sys
import math


# Initialization of programm
pygame.init()

# My clock
clock = pygame.time.Clock()

# The display that we will see
W, H = 1200, 800
display = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mussinka sdelal krug ura")

# Circle
pos = [W // 2, H // 2]
RED = (255, 0, 0)
r = 25
spd = 20


# Main code
run = True
while run:
    # Like just quit from programm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not run:
        break
    
    keys = pygame.key.get_pressed()

    right, left, up, down = 0, 0, 0, 0

    right = keys[pygame.K_RIGHT]
    left = keys[pygame.K_LEFT]
    up = keys[pygame.K_UP]
    down = keys[pygame.K_DOWN]

    display.fill((255, 255, 255))

    xadd = spd * (right - left)
    yadd = spd * (down - up)

    if pos[0] + xadd >= r and pos[0] + xadd <= W - r:
        pos[0] += xadd
    elif pos[0] + xadd < r:
        pos[0] = r
    elif pos[0] + xadd > W - r:
        pos[0] = W - r
    
    if pos[1] + yadd >= r and pos[1] + yadd <= H - r:
        pos[1] += yadd
    elif pos[1] + yadd < r:
        pos[1] = r
    elif pos[1] + yadd > H - r:
        pos[1] = H - r

    pygame.draw.circle(display, RED, pos, r)

    # Control the frame rate + Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()