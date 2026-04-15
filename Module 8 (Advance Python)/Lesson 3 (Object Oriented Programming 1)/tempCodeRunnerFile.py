import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple Robot Simulation')

WHITE = (255, 255, 255)
RED = (255, 0, 0)

robot_pos = [400, 300]
robot_size = 50
robot_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_pos[0] -= robot_speed
    if keys[pygame.K_RIGHT]:
        robot_pos[0] += robot_speed
    if keys[pygame.K_UP]:
        robot_pos[1] -= robot_speed
    if keys[pygame.K_DOWN]:
        robot_pos[1] += robot_speed

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (*robot_pos, robot_size, robot_size))

    pygame.display.flip()

    pygame.time.Clock().tick(30)