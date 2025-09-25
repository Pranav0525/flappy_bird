import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")


clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    clock.tick(FPS)
    screen.fill((135, 206, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT