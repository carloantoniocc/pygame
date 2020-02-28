import pygame
import sys

pygame.init()

width= 800
height= 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption('Colores')

## Sistema RGB Rojo verde y Azul
## pygame.color(R,G,B) 0-255
red = pygame.Color(255,0,0)
verde = pygame.Color(0,255,0)
azul = pygame.Color(0,0,255)

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
rosado = pygame.Color(200,90,130)

## surface2 = pygame.Surface( (200,200) )

## la funcion load nos retornara una superficie
codi = pygame.image.load('images/codi.png')
rect = codi.get_rect()
rect.center= (width // 2 , height // 2 )

rectangulo = pygame.image.load('images/small_rectangle.png')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(white)

    ##  surface.blit(codi, (100,1) )
	##surface.blit(codi, (100,100) )
	surface.blit(codi, rect )

	pygame.display.update()