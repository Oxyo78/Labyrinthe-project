# Fonction du fichier game.py
import pygame, os

def screen(SCREEN_WIDTH,SCREEN_HEIGHT):
	'''Création de la fenetre'''
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
	return screen

#Importation des textures
def background(screen_game):
	'''Texture de fond'''
	coor_spirite_x = 160
	coor_spirite_y = 220
	len_spirite_x = 20
	len_spirite_y = 20
	longueur_map_x = 300 # 15 zones * 20 pixels
	longueur_map_y = 300 # 15 zones * 20 pixels
	interval_map = 20

	background = pygame.image.load("Picture/floor-tiles-20x20.png")
	background.set_clip(pygame.Rect(coor_spirite_x, coor_spirite_y, len_spirite_x, len_spirite_y))
	draw_back = background.subsurface(background.get_clip())
	for x in range(0, longueur_map_x, interval_map):
		for y in range(0, longueur_map_y, interval_map):
			screen_game.blit(draw_back, (x,y))
	return background

