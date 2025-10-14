import pygame
import sys
import random

pygame.init()


gravity = 0.5
bird_velocity = 0
jump_strength = -10

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY BIRD")

clock = pygame.time.Clock()
FPS = 60

bird_x = 50
bird_y = 300
bird_width = 30
bird_height = 30
bird_color = (255, 255, 0)
pipe_width = 60
pipe_gap = 150
pipe_color = (0, 255, 0)
pipe_x = WIDTH
pipe_height = random.randint(100, 350)
pipe_speed = 3

score = 0
passed_pipe = False

font = pygame.font.SysFont(None, 36)

running = True
game_over = False


while running:
    clock.tick(FPS)
    screen.fill((135, 206, 250))

    if not game_over:
        bird_velocity += gravity
        bird_y += bird_velocity
        pipe_x -= pipe_speed

    bird_rect = pygame.draw.rect(screen, bird_color, (bird_x, bird_y, bird_width, bird_height))
    
    pipe_top = pygame.draw.rect(screen, pipe_color, (pipe_x, 0, pipe_width, pipe_height))

    pipe_bottom = pygame.draw.rect(screen, pipe_color, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))


    
    if pipe_x + pipe_width < bird_x and not passed_pipe:
        score += 1
        passed_pipe = True
        pipe_speed += 0.1
        if pipe_speed >= 10:
            pipe_speed = 10

    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 350)
        passed_pipe = False


    if bird_rect.colliderect(pipe_bottom) or bird_rect.colliderect(pipe_top) or bird_y > HEIGHT or bird_y < -50:
        game_over = True

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))


    if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    bird_velocity = jump_strength
                else:
                    bird_y = 300
                    bird_velocity = 0
                    pipe_x = WIDTH
                    pipe_height = random.randint(100, 350)
                    score = 0
                    passed_pipe = False
                    pipe_speed = 3
                    game_over = False

    pygame.display.update()

pygame.quit()
sys.exit()