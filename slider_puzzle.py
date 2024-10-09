import pygame
import random

# Constants
WINDOW_SIZE = 300
TILE_SIZE = 100
GRID_SIZE = 3
BACKGROUND_COLOR = (30, 30, 30)
TILE_COLOR = (200, 200, 200)
FONT_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
my_name = "YOUR NAME"
pygame.display.set_caption(f"{my_name}")
font = pygame.font.Font(None, 60)

# Helper function to draw a tile
def draw_tile(screen, tile, x, y):
    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, TILE_COLOR, rect)
    text = font.render(str(tile), True, FONT_COLOR)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

# Generate a random solvable puzzle
def generate_puzzle():
    numbers = list(range(1, GRID_SIZE * GRID_SIZE))
    numbers.append(0)  # Zero represents the empty tile
    random.shuffle(numbers)
    return [numbers[i:i + GRID_SIZE] for i in range(0, len(numbers), GRID_SIZE)]

# Get position of the empty tile
def get_empty_tile_position(puzzle):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if puzzle[row][col] == 0:
                return row, col

# Move a tile if it's adjacent to the empty space
def move_tile(puzzle, row, col):
    empty_row, empty_col = get_empty_tile_position(puzzle)
    if (abs(row - empty_row) + abs(col - empty_col)) == 1:  # Check if adjacent
        puzzle[empty_row][empty_col], puzzle[row][col] = puzzle[row][col], puzzle[empty_row][empty_col]

# Check if the puzzle is solved
def is_solved(puzzle):
    correct = list(range(1, GRID_SIZE * GRID_SIZE)) + [0]
    flat_puzzle = [tile for row in puzzle for tile in row]
    return flat_puzzle == correct

# Draw the entire puzzle
def draw_puzzle(screen, puzzle):
    screen.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            tile = puzzle[row][col]
            if tile != 0:  # Don't draw the empty space
                draw_tile(screen, tile, col * TILE_SIZE, row * TILE_SIZE)
    pygame.display.flip()

def main():
    puzzle = generate_puzzle()
    running = True
    won = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # TODO: Add an if-elif statement for save and load functions here (use 's' key for save, and 'l' key for load).
                if not won:  # Only allow moves if the game isn't solved
                    empty_row, empty_col = get_empty_tile_position(puzzle)
                    if event.key == pygame.K_UP and empty_row < GRID_SIZE - 1:
                        move_tile(puzzle, empty_row + 1, empty_col)
                    elif event.key == pygame.K_DOWN and empty_row > 0:
                        move_tile(puzzle, empty_row - 1, empty_col)
                    elif event.key == pygame.K_LEFT and empty_col < GRID_SIZE - 1:
                        move_tile(puzzle, empty_row, empty_col + 1)
                    elif event.key == pygame.K_RIGHT and empty_col > 0:
                        move_tile(puzzle, empty_row, empty_col - 1)

        if not won:
        # draw puzzle
            draw_puzzle(screen, puzzle)

            # Check if the puzzle is solved
            if is_solved(puzzle):
                won = True
                screen.fill(BACKGROUND_COLOR)
                text = font.render("You Win!", True, FONT_COLOR)
                text_rect = text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
                screen.blit(text, text_rect)
                pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
