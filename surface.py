import pygame

pygame.init()

width= 400
height= 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Hola mundo')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()