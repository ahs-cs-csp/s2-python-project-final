import pygame
import random
import string
import time
import requests

pygame.init()
# Step 1: How Big of a window?
WIDTH, HEIGHT = ..., ...
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boggle")

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

# Step #2: Look Up RGB codes for the missing colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = ...
GREEN = ...
RED = ...
BLUE = ...

BOGGLE_DICE = [
    "AAEEGN", "ABBJOO", "ACHOPS", "AFFKPS",
    "AOOTTW", "CIMOTU", "DEILRX", "DELRVY",
    "DISTTY", "EEGHNW", "EEINSU", "EHRTVW",
    "EIOSST", "ELRTTY", "HIMNQU", "HLNNRZ"
]

word_cache = {}

def is_valid_word(word):
    word = word.lower()
    if word in word_cache:
        return word_cache[word]
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(...)
    is_valid = response.status_code == 200
    word_cache[word] = is_valid
    return is_valid

# STEP 3: This returns a 4x4 list of lists of one random 
# letter from each "die" in BOGGLE_DICE
def generate_board():
    temp_board = []
    boggle_dice_index = 0
    for r in range(...):
        row = []
        for c in range(...):
            die = BOGGLE_DICE[...]
            row.append(die[random.randint(..., ...)])
            boggle_dice_index = ... + 1
        temp_board.append(...) 
            
    return temp_board

# STEP 4: return a score for each word length
def word_score(word):
    length = len(word)
    if length < 3:
        return 0
    elif length <= 4:
        return ...
    elif length == 5:
        return ...
    elif length == 6:
        return ...
    elif length == 7:
        return ...
    else:
        return ...

# STEP 5: get the letter from the board
# to put on the screen
def draw_board(board):
    cell_size = 100
    for row in range(4):
        for col in range(4):
            rect = pygame.Rect(col * cell_size + 50, row * cell_size + 50, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 3)
            letter = ...
            text = font.render("Qu" if letter == "Q" else letter, True, BLACK)
            screen.blit(text, (rect.x + 25, rect.y + 20))

def is_valid(word, board):
    word = word.upper()

    def dfs(x, y, word, visited):
        if not word:
            return True
        if x < 0 or y < 0 or x >= 4 or y >= 4 or (x, y) in visited:
            return False
        cell = board[x][y]
        if cell == 'Q':
            if not word.startswith('QU'):
                return False
            word = word[2:]
        else:
            if not word.startswith(cell):
                return False
            word = word[1:]
        visited.add((x, y))
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    if dfs(x + dx, y + dy, word, visited.copy()):
                        return True
        return False

    for i in range(4):
        for j in range(4):
            if dfs(i, j, word, set()):
                return True
    return False

# STEP 6: 6 "..." to complete
# - set the duration in seconds
# - big_font.render -- look pygame font render
# - Place the "Times Up!" line  in the middle of the screen
# - Set three appropriate messages for when:
#   - word has already been used, 
#   - when the word is valid, and 
#   - when the word given is not a word
def main():
    board = generate_board()
    input_word = ""
    found_words = set()
    score = 0
    message = ""
    start_time = time.time()
    duration = ...

    running = True
    while running:
        screen.fill(WHITE)

        elapsed = int(time.time() - start_time)
        remaining = max(0, duration - elapsed)
        timer_text = big_font.render(f"{remaining // 60}:{remaining % 60:02d}", True, BLUE)
        screen.blit(timer_text, (WIDTH // 2 - 40, 10))

        if remaining == 0:
            end_text = big_font.render("Times Up!", True, RED)
            screen.blit(end_text, (..., ...))
            pygame.display.flip()
            pygame.time.wait(4000)
            running = False
            continue

        draw_board(board)

        pygame.draw.rect(screen, BLACK, (50, 470, 500, 40), 2)
        word_surface = small_font.render(input_word, True, BLACK)
        screen.blit(word_surface, (60, 475))

        score_text = small_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (50, 530))

        msg_text = small_font.render(message, True, GREEN if "✓" in message else RED)
        screen.blit(msg_text, (50, 560))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and remaining > 0:
                if event.key == pygame.K_RETURN:
                    if input_word.upper() in found_words:
                        message = ...
                    elif is_valid_word(input_word) and is_valid(input_word, board):
                        found_words.add(input_word.upper())
                        points = word_score(input_word)
                        score += points
                        message = ...
                    else:
                        message = ...
                    input_word = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                elif event.unicode.isalpha():
                    input_word += event.unicode.upper()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    screen.fill(WHITE)
    final_text = big_font.render("Game Over!", True, BLACK)
    screen.blit(final_text, (WIDTH // 2 - 120, 250))
    final_score = font.render(f"Final Score: {score}", True, BLUE)
    screen.blit(final_score, (WIDTH // 2 - 100, 310))
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()

if __name__ == "__main__":
    main()
