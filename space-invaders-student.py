import pygame
import random
import math
import os

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Parson's Problem")

# STEP 1: Look up how to set the missing colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = ...
YELLOW = ...
GREEN = ...

# Fonts
font = pygame.font.SysFont(None, 36)
game_over_font = pygame.font.SysFont(None, 72)

# Player
player_width = 50
player_height = 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 6
player_x_change = 0

# Bullet
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = player_y
bullet_speed = 8
bullet_state = "ready"

# Enemies
enemy_width = 40
enemy_height = 30
num_of_enemies = 6
enemy_x = []
enemy_y = []
enemy_speed_x = []
enemy_speed_y = 40
base_enemy_speed = 3

for _ in range(num_of_enemies):
    enemy_x.append(random.randint(0, WIDTH - enemy_width))
    enemy_y.append(random.randint(50, 150))
    enemy_speed_x.append(base_enemy_speed)

# Score
score = 0
high_score_file = "highscore.txt"
if os.path.exists(high_score_file):
    with open(high_score_file, "r") as f:
        high_score = int(f.read())
else:
    high_score = 0

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_width, enemy_height))

def draw_bullet(x, y):
    pygame.draw.rect(screen, YELLOW, (x + player_width // 2 - bullet_width // 2, y, bullet_width, bullet_height))

def is_collision(ex, ey, bx, by):
    distance = math.hypot(ex + enemy_width // 2 - bx, ey + enemy_height // 2 - by)
    return distance < 27  # threshold for hit

def show_score():
    text = font.render(f"Score: {score}  High Score: {high_score}", True, WHITE)
    screen.blit(text, (10, 10))

def show_game_over():
    msg = game_over_font.render("GAME OVER", True, GREEN)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 50))
    restart_msg = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(restart_msg, (WIDTH // 2 - restart_msg.get_width() // 2, HEIGHT // 2 + 30))
    pygame.display.update()

# Game state
running = True
game_over = False

clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    if game_over:
        show_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_r:
                    score = 0
                    enemy_x = [random.randint(0, WIDTH - enemy_width) for _ in range(num_of_enemies)]
                    enemy_y = [random.randint(50, 150) for _ in range(num_of_enemies)]
                    enemy_speed_x = [base_enemy_speed for _ in range(num_of_enemies)]
                    player_x = WIDTH // 2 - player_width // 2
                    bullet_state = "ready"
                    bullet_y = player_y
                    game_over = False
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # STEP 2: player_speed controls the change in x; set the correct 
        #         change for left and rigt movement
        # Step 3: when the spacebar is pressed, the bullet should leave from the 
        #         player -- set up the bullet x, y and state. Look in the code
        #         for the two values that bullet_state should be set to
        # Step 4: what happens the arrows keys are released? Fix the KEYUP event
        #           below
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = ...
            elif event.key == pygame.K_RIGHT:
                player_x_change = ...
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = ...
                bullet_y = ...
                bullet_state = ...
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = ...

    player_x += player_x_change
    player_x = max(0, min(WIDTH - player_width, player_x))

    if bullet_state == "fire":
        draw_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"

    for i in range(num_of_enemies):
        enemy_x[i] += enemy_speed_x[i]

        # STEP 5: When the enemy hits the edge of the screen
        #           they reverse direction and move down the screen
        #           enemy_speed_y controls the y-direction of the enemies
        if enemy_x[i] <= 0 or enemy_x[i] >= WIDTH - enemy_width:
            enemy_speed_x[i] *= ...
            enemy_y[i] += ...

        if enemy_y[i] > HEIGHT - 100:
            game_over = True
            if score > high_score:
                with open(high_score_file, "w") as f:
                    f.write(str(score))
                high_score = score
            break

        # STEP 6: A bullet hits an enemy, set the bullet_y and
        #         bullet_state correctly 
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = ...
            bullet_state = ...
            score += 1

            if score % 5 == 0:
                for j in range(num_of_enemies):
                    enemy_speed_x[j] += 1 if enemy_speed_x[j] > 0 else -1

            enemy_x[i] = random.randint(0, WIDTH - enemy_width)
            enemy_y[i] = random.randint(50, 150)

        draw_enemy(enemy_x[i], enemy_y[i])

    draw_player(player_x, player_y)
    show_score()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
