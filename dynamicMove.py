import pygame
from pygame.locals import *

#Initialisation de pygame
pygame.init()
fenetre = pygame.display.set_mode((640, 480),RESIZABLE)
pygame.display.set_caption("NOM DU JEU")

#COULEUR
BLANC = (255,255,255)
NOIR =  (  0, 0, 0)

background = pygame.Surface((640,480))
background.fill(NOIR)

cubeMove = pygame.Surface((120,120))
cubeMove.fill(BLANC)
cubeRect = cubeMove.get_rect(topleft = (100,100))

cubeMove2 = pygame.Surface((120,120))
cubeMove2.fill(BLANC)
cubeRect2 = cubeMove2.get_rect(topleft = (200,200))

cube_drag = False

listecube = []
listecube.append(cubeRect)
listecube.append(cubeRect2)

#Boucle événementielle
continuer = True
while continuer:
	clock = pygame.time.Clock()
	for event in pygame.event.get():
		if event.type == QUIT:
				continuer = False

		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(listecube)):
					if listecube[i].collidepoint(event.pos):
						cube_drag = True
						offsetx = listecube[i].x - event.pos[0]
						offsety = listecube[i].y - event.pos[1]
						rect_indice = i
		elif event.type == MOUSEBUTTONUP:
			if event.button == 1:
				cube_drag = False
		elif event.type == MOUSEMOTION:
				if cube_drag:
					listecube[rect_indice].x = event.pos[0] + offsetx
					listecube[rect_indice].y = event.pos[1] + offsety
					print("coord x", listecube[rect_indice].x,"\ncoord y:", listecube[rect_indice].y)

	print(listecube)

	#L'affichage du jeu
	fenetre.blit(background,(0,0))
	fenetre.blit(cubeMove,cubeRect)
	fenetre.blit(cubeMove2,cubeRect2)

	#Rafraichissement
	pygame.display.flip()
	clock.tick(60)
