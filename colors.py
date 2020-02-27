import pygame
import sys

pygame.init()

width= 400
height= 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Colores')

# Sistema RGB Rojo verde y Azul
# pygame.color(R,G,B) 0-255
red = pygame.Color(255,0,0)
verde = pygame.Color(0,255,0)
azul = pygame.Color(0,0,255)

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
rosado = pygame.Color(200,90,130)

#TUPLAS
my_color = (200,90,130)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(my_color)
	pygame.display.update()