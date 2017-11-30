#coding:utf-8
#! /usr/bin/env python3

import pygame, os, random
from pygame.locals import *
import random
from fonction.map_generator import *
from fonction.texture_loader import *
from fonction.config import *


class LevelShow:
	"""Loading and generator of the map from LevelGame.txt """

	def __init__(self):
		self.map_list = []
		self.player_position = 0
		self.gardian_position = 0


	def get_the_map_list(self):
		#Get the map list from file
		self.map_list = map_initialize("LevelGame.txt", "map")

	

	def show_map(self, windows_screen):
		# get texture
		ground = texture_for_sprite("floor-tiles-20x20.png", "picture", 160, 220, 20, 20, 0)
		wall = texture_for_sprite("floor-tiles-20x20.png", "picture", 60, 60, 20, 20, 0)
		finnish = texture_for_sprite("floor-tiles-20x20.png", "picture", 160, 20, 20, 20, 1)

		# Show the map on windows
		line_number = 0
		for line in self.map_list:
			case_number = 0
			for letter in line:
				if letter == "M": # print a wall sprite
					windows_screen.blit(wall,(case_number*sprite_size, line_number*sprite_size))

				if letter == "G" or letter == "P" or letter == "B" : # print a ground sprite
					windows_screen.blit(ground,(case_number*sprite_size, line_number*sprite_size))

					if letter == "P": # Get the position of the player
						self.player_position = (case_number, line_number)

					if letter == "B": # Get the position of the gardian
						self.gardian_position = (case_number, line_number) 

				if letter == "A": # print a finnish sprite on a ground sprite ( transparent texture )
					windows_screen.blit(ground,(case_number*sprite_size, line_number*sprite_size))
					windows_screen.blit(finnish,(case_number*sprite_size, line_number*sprite_size))


				case_number += 1
			line_number += 1



class Character:
	""" initialize the character and control"""

	def __init__(self, character_position):
		# Get the position of the character form the map_list
		self.character_position_x, self.character_position_y = character_position
		# Get the size of the map in case
		self.lengh_map = map_size("LevelGame.txt", "map")
		self.lengh_map = self.lengh_map / sprite_size
	




	def character_texture(self, file_name, folder_file, pos_x_left_top, pos_y_left_top, size_x, size_y, alpha_sprite_file, red_color, green_color, blue_color):
		# Get texture of player
		self.character_texture = texture_for_sprite(file_name, folder_file, pos_x_left_top, pos_y_left_top, size_x, size_y, alpha_sprite_file, red_color, green_color, blue_color)

	def dead_texture(self, file_name, folder_file, pos_x_left_top, pos_y_left_top, size_x, size_y, alpha_sprite_file, red_color, green_color, blue_color):
		self.dead_texture = texture_for_sprite(file_name, folder_file, pos_x_left_top, pos_y_left_top, size_x, size_y, alpha_sprite_file, red_color, green_color, blue_color)
	
	def show_character(self, windows_screen, character_is_alive):
		# Print the charactere on map
		if character_is_alive == 1:
			windows_screen.blit(self.character_texture, (self.character_position_x * sprite_size, self.character_position_y * sprite_size))
		else:
			windows_screen.blit(self.dead_texture, (self.character_position_x * sprite_size, self.character_position_y * sprite_size))

	def player_control(self, direction, windows_screen, map_list):
		# Control the direction of th charactere wih keyboard Up, Down, Left, Right
		if  direction == "up":
			if self.character_position_y != 0: # Border up windows check
				if map_list[self.character_position_y - 1][self.character_position_x] != "M": # Wall collision check
					self.character_position_y -= 1 # Go up of 1 case

		if direction == "down":
			if self.character_position_y != self.lengh_map - 1: # Border down windows check
				if map_list[self.character_position_y + 1][self.character_position_x] != "M": # Wall collision check
					self.character_position_y += 1 # Go down of 1 case

		if direction == "right":
			if self.character_position_x != self.lengh_map - 1: # Border right windows check
				if map_list[self.character_position_y][self.character_position_x + 1] != "M": # Wall collision check
					self.character_position_x += 1 # Go right of 1 case
		
		if direction == "left":
			if self.character_position_x !=0: # Border left windows check
				if map_list[self.character_position_y][self.character_position_x - 1] != "M": # Wall collision check
					self.character_position_x -= 1 # go left of 1 case
			
	def character_proximity(self, player_position_x, player_position_y):
		# Proximity detection for event

		if (player_position_x, player_position_y) == (self.character_position_x -1, self.character_position_y):
			return 1
		elif (player_position_x, player_position_y) == (self.character_position_x +1, self.character_position_y):
			return 1
		elif (player_position_x, player_position_y) == (self.character_position_x, self.character_position_y -1):
			return 1	
		elif (player_position_x, player_position_y) == (self.character_position_x -1, self.character_position_y +1):
			return 1
		else:
			return 0

class GameObject:
	""" Initialize an game object """

	COUNT_OBJECT = 0 # Add 1 for each object created

	

	def __init__(self):		
		self.random_y = 0
		self.random_x = 0
		self.object_state = 1
		GameObject.COUNT_OBJECT += 1


	def object_texture(self, file_name, folder_file, pos_x_left_top, pos_y_left_top, size_x, size_y, alpha_sprite_file, red_color, green_color, blue_color):
		self.object_texture = texture_for_sprite(file_name, folder_file, pos_x_left_top, pos_y_left_top, size_x, size_y, alpha_sprite_file, red_color, green_color, blue_color)
		

	def random_position(self, map_list):
		self.random_loop = True
		self.random_y = 0
		self.random_x = 0

		while self.random_loop:
			"""get a random position for the oject"""

			self.random_y = random.randrange(0,14)
			self.random_x = random.randrange(0,14)
			if map_list[self.random_y][self.random_x] != "M":
				if map_list[self.random_y][self.random_x] != "B":
					if map_list[self.random_y][self.random_x] != "P": 					
						break
			else:
				continue

	def show_object(self, windows_screen):
		"""Show the item with the random position"""
		if self.object_state == 1: # if the item is no pick up, show him
			windows_screen.blit(self.object_texture, (self.random_x * 30, self.random_y * 30))



class GameEvent:
	# Game event

	def __init__(self):
		self.pickUp_object = GameObject.COUNT_OBJECT
		self.game_end = 1
		self.gardian_show = 1
		self.player_show = 1

	
	def victory(self, proximity_detection):
		
		if proximity_detection == 1:
			if self.pickUp_object == 0:
				self.gardian_show = 0
			else:
				self.player_show = 0
			self.game_end = 0









def main():
	pass



if __name__ == "__main__":
	main()

