#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *

BLANC = (255,255,255)
NOIR =  (  0, 0, 0)

#Initialisation de pygame
pygame.init()
fenetre = pygame.display.set_mode((640, 480),RESIZABLE)
pygame.display.set_caption("FPS PROTOTYPE")

perso = pygame.Surface((50,50))
perso_rect = perso.get_rect()

clock = pygame.time.Clock()

pixel_font_dir = "lib/font/Fipps-Regular.otf"
pixel_font = pygame.font.Font(pixel_font_dir, 15)

fps_text = pixel_font.render("FPS:" + str(round(clock.get_fps(),2)), True, NOIR)
fps_rect = fps_text.get_rect(topleft = (100,100))

pygame.key.set_repeat(1,30)
pygame.time.set_timer(USEREVENT, 1000)

#Boucle événementielle
continuer = True
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
				continuer = False
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				perso_rect.y += 10
			elif event.key == K_UP:
				perso_rect.y -= 10
		if event.type == USEREVENT:
			fps_text = pixel_font.render("FPS:" + str(round(clock.get_fps(),2)), True, NOIR)

	#L'affichage du jeu
	fenetre.fill(BLANC)
	fenetre.blit(perso, perso_rect)
	fenetre.blit(fps_text, fps_rect)

	#Rafraichissement
	pygame.display.flip()
	clock.tick()

