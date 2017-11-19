# Fonction du fichier game.py
import pygame, os

def screen(SCREEN_WIDTH,SCREEN_HEIGHT):
	'''Création de la fenetre'''
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], pygame.RESIZABLE)
	pygame.display.set_caption("Sauvez MacGyver !") 
	return screen

#Importation des textures
def background(screen_game):
	'''Texture de fond'''
	coor_spirite_x = 160 # coordonnee X du sprite
	coor_spirite_y = 220 # coordonnee Y du sprite
	len_spirite_x = 20 # Longeur en X du sprite
	len_spirite_y = 20 # Hauteur en Y du sprite
	longueur_map_x = 450 # 15 zones * 30 pixels
	longueur_map_y = 450 # 15 zones * 30 pixels
	interval_map = 30 # Intervalle de mappage

	background = pygame.image.load("Picture/floor-tiles-20x20.png").convert()
	background.set_clip(pygame.Rect(coor_spirite_x, coor_spirite_y, len_spirite_x, len_spirite_y))
	draw_back = background.subsurface(background.get_clip())
	draw_back = pygame.transform.scale(draw_back,(30,30)) # Convertion du sprit 20*20 en 30*30 pixels
	for x in range(10, longueur_map_x, interval_map):
		for y in range(10, longueur_map_y, interval_map):
			screen_game.blit(draw_back, (x,y))
	return background

def player(screen_game):
	'''affichage du joueur'''

	img_macgyver = pygame.image.load("Picture/MacGyver.png").convert_alpha()
	img_player = pygame.transform.scale(img_macgyver,(30, 30))
	screen_game.blit(img_player, (100,100))
	return img_player

def gardien(screen_game):
	'''affichage du gardien'''

	img_gardien = pygame.image.load("Picture/Gardien.png").convert_alpha()
	img_gardien2 = pygame.transform.scale(img_gardien,(30, 30))
	screen_game.blit(img_gardien2, (140,170))
	return img_gardien2

