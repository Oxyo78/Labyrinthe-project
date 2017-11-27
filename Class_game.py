#coding:utf-8

import pygame, os
from pygame.locals import *
import random


class LevelGenerator:
	"""Loading and generator of the map from LevelGame.txt """

	def __init__(self):
		self.level_design = 0 # List from LevelGame.txt
		self.wall_pos = [] # List from walls positions
		self.ground_pos = [] # List from ground positions


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
		wall_list = [] # Wall colision list
		ground_list = [] # Ground list


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
					wall_list.append((coor_x, coor_y)) # Add X and Y position to the wall colision list

				if letter == "G":
					windows_screen.blit(ground, (coor_x, coor_y))
					ground_list.append((coor_x, coor_y)) # Add X and Y positions to the ground position list

				if letter == "A":
					windows_screen.blit(ground, (coor_x, coor_y))
					windows_screen.blit(finish, (coor_x, coor_y))
				coor_x += 30
			coor_y += 30
			coor_x = 10
		self.wall_pos = wall_list
		self.ground_pos = ground_list



class Character:
	'''Initialize of toons'''

	def __init__(self, texture, pos_x, pos_y):
		self.texture = texture
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.toon = 0

	def characterPosition(self,windows_screen):
		# Get texture and convert
		texture = pygame.image.load(self.texture).convert()
		texture_character = texture.subsurface(texture.get_clip())
		texture_character = pygame.transform.scale(texture_character,(30,30))
		texture_character.set_colorkey((0, 0, 0))
		
		# Show character on windows
		windows_screen.blit(texture_character,(self.pos_x, self.pos_y))
		self.toon = texture_character

	def mouvement(self, direction, windows_screen, wallPosition):
		# player control
		if direction == "up":

			if self.pos_y - 30 < 10: # Windows border colision test
				self.pos_y = self.pos_y
			else: # Move to 
				self.pos_y = self.pos_y - 30
			for x, y in wallPosition: # Wall colision test
				if (x, y) == (self.pos_x, self.pos_y):
					self.pos_y = self.pos_y + 30
					break

		if direction == "down":
			if self.pos_y + 30 > 430 :
				self.pos_y = self.pos_y
			else:
				self.pos_y = self.pos_y + 30
			for x, y in wallPosition:
				if (x, y) == (self.pos_x, self.pos_y):
					self.pos_y = self.pos_y - 30
					break

		if direction == "right":
			if self.pos_x + 30 > 430:
				self.pos_x = self.pos_x
			else:
				self.pos_x = self.pos_x + 30
			for x, y in wallPosition:
				if (x, y) == (self.pos_x, self.pos_y):
					self.pos_x = self.pos_x - 30
					break

		if direction == "left":
			if self.pos_x - 30 < 10:
				self.pos_x = self.pos_x
			else:
				self.pos_x = self.pos_x - 30
			for x, y in wallPosition:
				if (x, y) == (self.pos_x, self.pos_y):
					self.pos_x = self.pos_x + 30
					break

		windows_screen.blit(self.toon, (self.pos_x, self.pos_y))
		pygame.display.flip()

class ItemMap:
	"""Get object and show in random position"""
	OBJECT_COUNT = 0

	def __init__(self, texture):
		self.texture = texture
		self.object_position = []
		ItemMap.OBJECT_COUNT += 1
		print(ItemMap.OBJECT_COUNT)

	def random_position(self, groundPosition):
		
		object_position = []
		object_position = random.sample(groundPosition, 3)
		self.object_position = object_position
		for x in range(3):
			print("object_position{} : {}".format(x, object_position[x]))

	def affichageObject(self, rect_x, rect_y, object_position, windows_screen):
		texture1 = pygame.image.load(self.texture).convert()
		texture1.set_clip(pygame.Rect(rect_x, rect_y, 32, 32))
		Object1 = texture1.subsurface(texture1.get_clip())
		Object1.set_colorkey((0, 0, 0))
		Object1 = pygame.transform.scale(Object1,(30,30))	
		windows_screen.blit(Object1,self.object_position[object_position])
		pygame.display.flip()
		
		
