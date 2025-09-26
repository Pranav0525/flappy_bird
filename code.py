import pygame
import sys

pygame.init()

bird_x = 50
bird_y = 300
bird_width = 30
bird_height = 30
bird_color = (255, 255, 0)

gravity = 0.5
bird_velocity = 0
jump_strength = -10

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")


clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    clock.tick(FPS)
    screen.fill((135, 206, 250))
    bird_velocity += gravity
    bird_y += bird_velocity

    pygame.draw.rect(screen, bird_color, (bird_x, bird_y, bird_width, bird_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength
        
    pygame.display.update()

pygame.quit()
sys.exit()