import pygame, os
from pygame.locals import *

#Variables
game_running = True
screen_width=640
screen_height=470



class LevelGenerator:
	"""Loading and generator of the map from LevelGame.txt """

	def __init__(self):
		self.level_design = 0


	def map_generator(self):
		with open("LevelGame.txt", "r") as file:
			file_list = [] 
			for line in file:
				line_list = []
				line.rstrip("\n")

				file_list.append(line)
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


windows_screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Sauvez MacGyver !")
pygame.key.set_repeat(400,30) 

map = LevelGenerator()
map.map_generator()
map.affichage(windows_screen)

pygame.display.flip()




while game_running:
	for event in pygame.event.get():
			#pygame prend le premier évènement de la file
			if event.type==QUIT:
			#l'évènement QUIT correspond au clic sur la croix
				game_running = 0