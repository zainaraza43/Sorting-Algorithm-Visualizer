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
sort = False
# Sorting algorithms
algos = ["Bubble Sort","Insertion Sort"]
index = 0
currentAlgo = algos[index]

def AppointSelected(list, item, colour):
	for l in list:
		if l == item:
			l.colour = colour
		else:
			l.colour = WHITE

def BubbleSort(list):

	for i in range(len(list)):
		for j in range(0,len(list)-i-1):

			AppointSelected(list, list[j], RED)

			for bar in bars:
				pygame.event.pump()
				pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10,500 - bar.value*10, 10, bar.value * 10))
				pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))
				pygame.display.flip()

			if list[j].value > list[j+1].value:
				list[j], list[j+1] = list[j+1], list[j]

	for bar in bars:
		pygame.draw.rect(screen, GREEN, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 10))
		pygame.time.delay(15)
		pygame.display.flip()

pygame.init()

#Font
font = pygame.font.SysFont("arial", 24)
currentAlgoText = font.render("Current Algorithm:", True, WHITE)
 
# Set the width and height of the screen [width, height]
size = (500, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sorting Algorithm Visualizer")
 
# Loop until the user clicks the close button.
done = False
 
# -------- Main Program Loop -----------
screen.fill(BLACK)
while not done:
	# --- Main event loop
	for event in pygame.event.get():

		if event.type == pygame.QUIT: # If Someone exits the window
			done = True

		if event.type == pygame.KEYDOWN: # If a key is pressed down

			if event.key == pygame.K_ESCAPE: # If escape is pressed
				done = True

			if event.key == pygame.K_RETURN: # If enter is pressed
				if sort:
					random.shuffle(bars)
					print("shuffled")
					sort = False
				if currentAlgo == "Bubble Sort":
					BubbleSort(bars)
				sort = True

			if event.key == pygame.K_RIGHT: # If right arrow is pressed
				sort = False
				random.shuffle(bars)
				if index == len(algos) - 1:
					index = 0
				else:
					index = index + 1

			if event.key == pygame.K_LEFT: # If left arrow is pressed
				sort = False
				random.shuffle(bars)
				if index == 0:
					index = len(algos) - 1
				else:
					index = index - 1


	for bar in bars:
		pygame.draw.rect(screen, WHITE, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 10))
		pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))

	# UI Stuff

	currentAlgo = algos[index]

	screen.blit(currentAlgoText,(5,500))
	pygame.draw.rect(screen, BLACK, pygame.Rect(220,500,200,25))
	screen.blit(font.render(currentAlgo, True, WHITE),(220,500))

	pygame.display.flip()

# Close the window and quit.
pygame.quit()