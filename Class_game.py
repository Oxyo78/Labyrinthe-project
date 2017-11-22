import pygame, os
from pygame.locals import *


class LevelGenerator:
	"""Loading and generator of the map from LevelGame.txt """

	def __init__(self):
		self.level_design = 0


	def map_generator(self):
		with open("LevelGame.txt", "r") as file:
			file_list = [] 
			for line in file:
				line_list = []
				for letter in line:
					if letter != "\n":
						line_list.append(letter)
				file_list.append(line_list)
			self.level_design = file_list

	
	def affichage(self, windows_screen):
		coor_x = 10 # Cordinate X of the sprite
		coor_y = 10 # Cordinate Y of the sprite
		sprite_size = 30

		# Get texture and scale 30*30
		ground_texture = pygame.image.load("Picture/floor-tiles-20x20.png").convert()
		wall_texture = pygame.image.load("Picture/floor-tiles-20x20.png").convert()
		finish_texture = pygame.image.load("Picture/depart.png").convert()
		ground_texture.set_clip(pygame.Rect(160, 220, 20, 20))
		wall_texture.set_clip(pygame.Rect(40, 60, 20, 20))
		ground = ground_texture.subsurface(ground_texture.get_clip())
		wall = wall_texture.subsurface(wall_texture.get_clip())
		finish = finish_texture.subsurface(finish_texture.get_clip())
		finish.set_colorkey((0,0,0)) # Convertion in alpha of "depart" texture
		ground = pygame.transform.scale(ground,(30,30)) # Convertion of the sprit 20*20 in 30*30 pixels
		wall = pygame.transform.scale(wall,(30,30)) # Convertion of the sprit 20*20 in 30*30 pixels

		for line in self.level_design:
			for letter in line:
				if letter == "M":
					windows_screen.blit(wall, (coor_x, coor_y))
				if letter == "G":
					windows_screen.blit(ground, (coor_x, coor_y))
				if letter == "A":
					windows_screen.blit(ground, (coor_x, coor_y))
					windows_screen.blit(finish, (coor_x, coor_y))
				coor_x += 30
			coor_y += 30
			coor_x = 10


"""m = LevelGenerator()
m.map_generator()
m.affichage(windows_screen)"""
#print(m.level_design)