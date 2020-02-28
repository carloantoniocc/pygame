import pygame
import sys

pygame.init()

width= 400
height= 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Hola mundo')

red = pygame.Color(255,0,0)
verde = pygame.Color(0,255,0)
azul = pygame.Color(0,0,255)

## para obtener el rectangulo de una superficie
rect = surface.get_rect()
rect.center = ( width // 2, height // 2)

## superficie2
## pygame.surface( (width ,height) )
surface2 = pygame.Surface( (200,200) )
surface2.fill(azul)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(verde)
	
	## surface.blit(surface2, (x,y) )
	surface.blit(surface2, (100,1) )

	pygame.draw.rect(surface2, red, (100,50,80,40) )

	pygame.display.update()
