import pygame
from pygame.locals import *

#Initialisation de pygame
pygame.init()
fenetre = pygame.display.set_mode((640, 480),RESIZABLE)
pygame.display.set_caption("NOM DU JEU")

#COULEUR
BLANC = (255,255,255)
NOIR =  (  0, 0, 0)

joueur = pygame.Surface((20,20))
joueur.fill(NOIR)

joueurRect = joueur.get_rect()

joueurRect.x = 100
joueurRect.y = 160

back1 = pygame.image.load("lib/image/background1.png").convert_alpha()
back2 = pygame.image.load("lib/image/background2.png").convert_alpha()
back3 = pygame.image.load("lib/image/background3.png").convert_alpha()
back4 = pygame.image.load("lib/image/background4.png").convert_alpha()
front1 = pygame.image.load("lib/image/foreground.png").convert_alpha()


back1 = pygame.transform.scale(back1,(1424 * 3, 368 * 3))
back2 = pygame.transform.scale(back2,(1424 * 3, 368 * 3))
back3 = pygame.transform.scale(back3,(1424 * 3, 368 * 3))
back4 = pygame.transform.scale(back4,(1424 * 3, 368 * 3))
front1 = pygame.transform.scale(front1,(1424 * 3, 368 * 3))

back1Rect = back1.get_rect()
back2Rect = back2.get_rect()
back3Rect = back3.get_rect()
back4Rect = back4.get_rect()
front1Rect = front1.get_rect()

pygame.key.set_repeat(1,30)

#Boucle événementielle
continuer = True
while continuer:
	clock = pygame.time.Clock()
	for event in pygame.event.get():
		if event.type == QUIT:
				continuer = False

		#plus l'objet graphique est loin plus il bouge lentement
		#attention si un objet graphique plus proche qu'un autre bouge moins vite alors il y aura un bug graphique
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				joueurRect.x -= 8
			if event.key == K_RIGHT:
				joueurRect.x += 8
			if event.key == K_UP:
				joueurRect.y -= 8
			if event.key == K_DOWN:
				joueurRect.y += 8


	#à gauche
	if joueurRect.x < 120:
		joueurRect.x = 120
		back1Rect.x += 6
		back2Rect.x += 5
		back3Rect.x += 4
		back4Rect.x += 3
		front1Rect.x += 8

	#à droite
	if joueurRect.x > 400:
		joueurRect.x = 400
		back1Rect.x += -6
		back2Rect.x += -5
		back3Rect.x += -4
		back4Rect.x += -3
		front1Rect.x += -8

	#en haut
	if joueurRect.y < 150:
		joueurRect.y = 150
		back1Rect.y += 6
		back2Rect.y += 5
		back3Rect.y += 4
		back4Rect.y += 3
		front1Rect.y += 8

	#en bas
	if joueurRect.y > 200:
		joueurRect.y = 200
		back1Rect.y += -6
		back2Rect.y += -5
		back3Rect.y += -4
		back4Rect.y += -3
		front1Rect.y += -8


	fenetre.blit(back4, back4Rect)
	fenetre.blit(back3, back3Rect)
	fenetre.blit(back2, back2Rect)
	fenetre.blit(back1, back1Rect)
	fenetre.blit(front1, front1Rect)
	fenetre.blit(joueur, joueurRect)




	#Rafraichissement
	pygame.display.flip()
	clock.tick(120)
