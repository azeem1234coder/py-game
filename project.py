import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Control")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the rectangles (sprites)
sprite1 = pygame.Rect(100, 100, 50, 50)  # Static sprite
sprite2 = pygame.Rect(300, 300, 50, 50)  # Movable sprite

# Speed for sprite movement
sprite2_speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Control for sprite2 (movable sprite)
    if keys[pygame.K_LEFT]:
        sprite2.x -= sprite2_speed
    if keys[pygame.K_RIGHT]:
        sprite2.x += sprite2_speed
    if keys[pygame.K_UP]:
        sprite2.y -= sprite2_speed
    if keys[pygame.K_DOWN]:
        sprite2.y += sprite2_speed

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the sprites (rectangles)
    pygame.draw.rect(screen, RED, sprite1)  # Static red sprite
    pygame.draw.rect(screen, BLUE, sprite2)  # Movable blue sprite

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
