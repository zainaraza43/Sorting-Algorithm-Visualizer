import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

numbers = []

for i in range(1,1000):
	numbers.append(i)

random.shuffle(numbers)

print(numbers)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Visualizer")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(BLACK)
 
    
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()