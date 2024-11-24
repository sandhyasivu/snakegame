import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
FPS = 15
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Snake Setup
snake = [(100, 100), (80, 100), (60, 100)]  # initial snake body
snake_dir = (CELL_SIZE, 0)  # initial direction (right)
snake_speed = 10

# Food Setup
food_x = random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE
food_y = random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE

# Score Setup
score = 0
font = pygame.font.SysFont('arial', 30)

# Game Over Function
def game_over():
    global score
    game_over_text = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(game_over_text, [WIDTH / 6, HEIGHT / 3])
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main Game Loop
def game_loop():
    global snake, snake_dir, food_x, food_y, score

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                    snake_dir = (-CELL_SIZE, 0)
                if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                    snake_dir = (CELL_SIZE, 0)
                if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                    snake_dir = (0, -CELL_SIZE)
                if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                    snake_dir = (0, CELL_SIZE)

        # Move Snake
        head_x, head_y = snake[0]
        new_head = (head_x + snake_dir[0], head_y + snake_dir[1])
        snake = [new_head] + snake[:-1]

        # Check if Snake Eats Food
        if new_head == (food_x, food_y):
            snake.append(snake[-1])  # Add a new segment to the snake
            food_x = random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE
            food_y = random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE
            score += 10

        # Check for Collisions with Walls
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            game_over()

        # Check for Collisions with Itself
        if new_head in snake[1:]:
            game_over()

        # Fill Screen with Background Color
        screen.fill(BLUE)

        # Draw Snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Draw Food
        pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, CELL_SIZE, CELL_SIZE))

        # Display Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        # Update the Display
        pygame.display.update()

        # Set Game Speed
        clock.tick(FPS)

# Run the Game
game_loop()
