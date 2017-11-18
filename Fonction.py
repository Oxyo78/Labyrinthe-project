# Fonction du fichier game.py
import pygame, os

def screen(SCREEN_WIDTH,SCREEN_HEIGHT):
	'''Création de la fenetre'''
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
	return screen

#Importation des textures
def background(screen_game):
	background = pygame.image.load("Picture/floor-tiles-20x20.png").convert()
	screen_game.blit(background, (0,0))
	return background

