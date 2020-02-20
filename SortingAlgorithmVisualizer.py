import pygame
import random
import time

class Bar:

	def __init__(self, value, colour):
		self.value = value
		self.colour = colour
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Random numbers to be sorted
bars = []

for i in range(1,1000):
	bars.append(Bar(i,WHITE))

random.shuffle(bars)


# Sorting algorithms
algos = ["Bubble Sort"]
currentAlgo = "Bubble Sort"

def Swap(item1, item2):
	temp = item1
	item1 = item2
	item2 = temp

def BubbleSort(list):
	for i in range(len(list)):
		for j in range(0,len(list)-i-1):
			if list[j].value > list[j+1].value:
				list[j], list[j+1] = list[j+1], list[j]
		if (i % 5 == 0) or (i == (len(list) - 1)):
			for bar in bars:
				pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar) + 1, 1000 - bar.value, 1, bar.value))
				pygame.display.flip()
		if i != (len(list) - 1):
			print(i, len(list))
			screen.fill(0)

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
screen.fill(BLACK)
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	if currentAlgo in algos:
		if currentAlgo == "Bubble Sort":
			BubbleSort(bars)
		currentAlgo = "None"


	pygame.display.flip()

	# Limit to 60 frames per second
	# clock.tick(60)

# Close the window and quit.
pygame.quit()
