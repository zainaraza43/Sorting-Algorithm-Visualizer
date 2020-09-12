import pygame
import random
import time

pygame.init()

class Bar:
	def __init__(self, value, colour):
		self.value = value
		self.colour = colour
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Font
font = pygame.font.SysFont("arial", 24)

# Random numbers to be sorted
bars = []

for i in range(1,51):
	bars.append(Bar(i,WHITE))

random.shuffle(bars)
sort = False

# Sorting algorithms
algos = ["Bubble Sort","Insertion Sort","Merge Sort"]
index = 0
currentAlgo = algos[index]

def BubbleSelected(list, item, colour):
	for l in list:
		if l == item:
			l.colour = colour
		else:
			l.colour = WHITE

def InsertionSelected(list, item1, item2):
	for l in list:
		if l == item1:
			l.colour = RED
		elif l == item2:
			l.colour = GREEN
		else:
			l.colour = WHITE

def ResetSelected(list):
	for l in list:
		l.colour = WHITE

def BubbleSort(list):
	
	comparisons = 0
	swaps = 0

	for i in range(len(list)):
		for j in range(0,len(list)-i-1):

			BubbleSelected(list, list[j], RED)

			pygame.draw.rect(screen, BLACK, pygame.Rect(250,530,50,25))
			comparisons += 1
			screen.blit(font.render(str(comparisons), True, WHITE),(250,530))

			for bar in bars:
				pygame.event.pump()
				pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))
				pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10,500 - bar.value*10, 10, bar.value * 10))
				pygame.display.flip()

			if list[j].value > list[j+1].value:
				list[j], list[j+1] = list[j+1], list[j]
				pygame.draw.rect(screen, BLACK, pygame.Rect(250,560,50,25))
				swaps += 1
				screen.blit(font.render(str(swaps), True, WHITE),(250,560))

	for bar in bars:
		pygame.draw.rect(screen, GREEN, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 10))
		pygame.time.delay(15)
		pygame.display.flip()

	ResetSelected(list)

def InsertionSort(list):

	comparisons = 0
	swaps = 0

	for i in range(1, len(list)):

		comparisons += 1

		j = i
		while j > 0 and list[j-1].value > list[j].value:

			InsertionSelected(list, list[j], list[i])
			comparisons += 1
			swaps += 1

			pygame.draw.rect(screen, BLACK, pygame.Rect(250,530,50,25))
			pygame.draw.rect(screen, BLACK, pygame.Rect(250,560,50,25))
			screen.blit(font.render(str(comparisons), True, WHITE),(250,530))
			screen.blit(font.render(str(swaps), True, WHITE),(250,560))

			for bar in bars:
				pygame.event.pump()
				pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))
				pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10,500 - bar.value*10, 10, bar.value * 10))
				pygame.time.delay(1)
				pygame.display.flip()

			list[j], list[j-1] = list[j-1], list[j]
			j -= 1

	ResetSelected(list)

	for bar in bars: # Weird solution to bar colour bug (find a better fix later)
		pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))
		pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10,500 - bar.value*10, 10, bar.value * 10))
		pygame.display.flip()

	for bar in bars:
		pygame.draw.rect(screen, GREEN, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 10))
		pygame.time.delay(15)
		pygame.display.flip()
		
def MergeSort(list, comparisons = 0, swaps = 0):

	if len(list) > 1:

		mid = len(list) // 2
		L = list[:mid]
		R = list[mid:]

		MergeSort(L, comparisons, swaps)
		MergeSort(R, comparisons, swaps)

		i = j = k = 0

		while i < len(L) and j < len(R):

			for bar in bars:
				pygame.event.pump()
				pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))
				pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10,500 - bar.value*10, 10, bar.value * 10))
				pygame.display.flip()
			
			if L[i].value < R[j].value:
				list[k] = L[i]
				i += 1
			else:
				list[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			list[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			list[k] = R[j]
			j += 1
			k += 1


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
					sort = False
				if currentAlgo == "Bubble Sort":
					BubbleSort(bars)
				elif currentAlgo == "Insertion Sort":
					InsertionSort(bars)
				elif currentAlgo == "Merge Sort":
					MergeSort(bars)
				sort = True

			if event.key == pygame.K_RIGHT: # If right arrow is pressed
				if sort:
					random.shuffle(bars)
					sort = False
				if index == len(algos) - 1:
					index = 0
				else:
					index = index + 1

			if event.key == pygame.K_LEFT: # If left arrow is pressed
				if sort:
					random.shuffle(bars)
					sort = False
				if index == 0:
					index = len(algos) - 1
				else:
					index = index - 1


	for bar in bars:
		pygame.draw.rect(screen, bar.colour, pygame.Rect(bars.index(bar)*10, 500 - bar.value*10, 10, bar.value * 10))
		pygame.draw.rect(screen, BLACK, pygame.Rect(bars.index(bar)*10, 0, 10, 500-bar.value*10))

	# UI Stuff

	currentAlgo = algos[index]

	screen.blit(font.render("Current Algorithm:", True, WHITE),(5,500))
	pygame.draw.rect(screen, BLACK, pygame.Rect(220,500,200,30))
	screen.blit(font.render(currentAlgo, True, WHITE),(220,500))
	screen.blit(font.render("Comparisons:", True, WHITE),(5,530))
	screen.blit(font.render("Swaps:", True, WHITE),(5,560))
	pygame.display.flip()

# Close the window and quit.
pygame.quit()