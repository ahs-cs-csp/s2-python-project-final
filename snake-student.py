import pygame
import time
import random

pygame.init()

# STEP 1: Look up RGB Values for these colors
white = (255, 255, 255)
black = (0, 0, 0)
red = ...
green = ...
blue = ...

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

    # STEP 2: snake head coordinates should be in the middle of the screen
    # based on the width and height
    x1 = ...
    y1 = ...
 
    x1_change = 0
    y1_change = 0

    snake = []
    snake_length = 1

    # Step 3: We need a random spot on the screen; the cell size is 20
    # and the width and height are 600 and 400 repsectively. The problem is
    # that you need to have the food coordinates be on multiples of 20 
    # (e.g. 0, 20, 40, etc) - work out the math
    foodx = round(random.randrange(0, ... - cell_size) / ...) * ...
    foody = round(random.randrange(0, ... - cell_size) / ...) * ...

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            your_score(snake_length - 1)
            pygame.display.update()

            # STEP 4: 
            # - when "q" is pressed the game should stop but still be
            #   in a mode that you can continue playing. Two fields control
            #   this behavior: game_over and game_close. Study how these two fields
            #   are used and implement them below
            # - when "c" is pressed you should play  again. The last line of code
            #   in this file should give you an idea as to what to do when "c"
            #   is pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = ...
                        game_over = ...
                    elif event.key == pygame.K_c:
                        ...
        # Step 5: Figure out how movement works; the field cell_size is
        #           the distance of the change in the x or y direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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

        # STEP 6: You just implemented movement in Step #5 - use the fields
        #           you set here
        x1 += ...
        y1 += ...
        game_display.fill(black)
        pygame.draw.rect(game_display, green, [foodx, foody, cell_size, cell_size])

        snake_head = [x1, y1]
        snake.append(snake_head)

        if len(snake) > snake_length:
            del snake[0]

        # Step #7: you hit yourself! set game_close correctly
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = ...

        for block in snake:
            pygame.draw.rect(game_display, blue, [block[0], block[1], cell_size, cell_size])

        your_score(snake_length - 1)
        pygame.display.update()

        # STEP #8: What happens when you hit the food?
        #           - the food moves to a random spot - you did this earlier in the code
        #           - snake_length increases
        if x1 == foodx and y1 == foody:
            foodx = ...
            foody = ...
            snake_length += ...

        clock.tick(10)

    pygame.quit()
    quit()

game_loop()
