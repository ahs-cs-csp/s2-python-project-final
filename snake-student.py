import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

width, height = 600, 400
cell_size = 20
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 30)

def message(msg, color, y_offset=0):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3 + y_offset])

def your_score(score):
    value = score_font.render(f"Score: {score}", True, white)
    game_display.blit(value, [0, 0])

def game_loop():
    game_over = False
    game_close = False

    x1 = ...
    y1 = ...

    x1_change = ...
    y1_change = ...

    snake = []
    snake_length = 1

    foodx = ...
    foody = ...

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        ...
                    elif event.key == pygame.K_c:
                        ...

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ...
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = ...
                    y1_change = ...
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = ...
                    y1_change = ...
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = ...
                    x1_change = ...
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = ...
                    x1_change = ...

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += ...
        y1 += ...
        game_display.fill(black)
        pygame.draw.rect(game_display, green, [foodx, foody, cell_size, cell_size])

        snake_head = [x1, y1]
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == snake_head:
                ...

        for block in snake:
            pygame.draw.rect(game_display, blue, [block[0], block[1], cell_size, cell_size])

        your_score(snake_length - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = ...
            foody = ...
            snake_length += ...

        clock.tick(10)

    pygame.quit()
    quit()

game_loop()
