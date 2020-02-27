import pygame
import sys

pygame.init()

width= 400
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

## Rectangulo 1
## pygame.Rect(x,y,width,height)
rect = pygame.Rect(100,150,120,60)
rect.center = (width // 2, height // 2)

print (rect.x)
print (rect.y)

## Rectangulo 2 -- creado como tupla sin las caracteristicas de una tupla
rect2 = (100,100,80,40)

##TUPLAS
my_color = (200,90,130)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	surface.fill(verde)

	pygame.draw.rect(surface,red,rect)
	pygame.draw.rect(surface,azul,rect2)

	pygame.display.update()