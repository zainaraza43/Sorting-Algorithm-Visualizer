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

for i in range(1,51):
	bars.append(Bar(i,WHITE))

random.shuffle(bars)

# Sorting algorithms
algos = ["Bubble Sort"]
currentAlgo = "Bubble Sort"

def AppointSelected(list, item1, item2, colour):
	for l in list:
		if l == item1 or l == item2:
			l.colour = colour
		else:
			l.colour = WHITE

def AppointSelected(list, item, colour):
	for l in list:
		if l == item:
			l.colour = colour
		else:
			l.colour = WHITE

def BubbleSort(list):

	rectsList = []

	for i in range(len(list)):
		for j in range(0,len(list)-i-1):

			AppointSelected(list, list[j], RED)
			screen.fill(BLACK)

			for bar in bars:
				pygame.event.pump()
				pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 50))
				pygame.display.flip()

			if list[j].value > list[j+1].value:
				AppointSelected(list,list[j],list[j+1],)
				list[j], list[j+1] = list[j+1], list[j]

	for bar in bars:
		pygame.draw.rect(screen, GREEN, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 50))
		pygame.time.delay(15)
		pygame.display.flip()

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sorting Algorithm Visualizer")
 
# Loop until the user clicks the close button.
done = False
 
# -------- Main Program Loop -----------
screen.fill(BLACK)
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True

	if currentAlgo in algos:
		if currentAlgo == "Bubble Sort":
			BubbleSort(bars)
		currentAlgo = "None"

	pygame.display.flip()

# Close the window and quit.
pygame.quit()