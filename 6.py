import pygame
import random
# Initialize Pygame
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")
# Define colors
RED = (0, 255, 0)
# Ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = random.randint(ball_radius, screen_height - ball_radius)
speed_x = random.randint(-5, 5)
speed_y = random.randint(-5, 5)
# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Move the ball
    ball_x += speed_x
    ball_y += speed_y
    # Bounce off the edges
    if ball_x - ball_radius < 0 or ball_x + ball_radius > screen_width:
        speed_x = -speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > screen_height:
        speed_y = -speed_y
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    # Update the display
    pygame.display.flip()
    clock.tick(150) # Limit the frame rate to 60 FPS
# Quit Pygame
pygame.quit()
