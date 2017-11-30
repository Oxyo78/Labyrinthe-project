#coding:utf-8
#! /usr/bin/env python3

from class_game import *
import pygame, os
from pygame.locals import *
from fonction.map_generator import map_size
from fonction.config import *

"""Main file of the game"""

# Variable
game_running = 1 # loop game


# Get the size of the screen from the file map
lengh_windows = map_size("LevelGame.txt", "map")

# initialize the windows, name and keydown loop
windows_screen = pygame.display.set_mode([int(lengh_windows), int(lengh_windows)])
pygame.display.set_caption("Sauvez MacGyver !")
pygame.key.set_repeat(400,30) 

# Print the map on windows
map = LevelShow()
map.get_the_map_list()
map.show_map(windows_screen)

# Initialise the player class
player = Character(map.player_position)
player.character_texture("Macgyver.png", "picture", 0, 0, 32, 43, 1, 0, 0, 0)
player.dead_texture("extras-32x-32.png", "picture", 192, 0, 32, 32, 1, 0, 0, 0)

# Initialize the gardian class
gardian = Character(map.gardian_position)
gardian.character_texture("Gardien.png", "picture", 0, 0, 32, 36, 1, 0, 0, 0)
gardian.dead_texture("extras-32x-32.png", "picture", 192, 0, 32, 32, 1, 0, 0, 0)

#Object 1
object_Game1 = GameObject()
object_Game1.object_texture("extras-32x-32.png", "picture", 0, 0, 32, 32, 1, 0, 0, 0)
object_Game1.random_position(map.map_list)

#Object 2
object_Game2 = GameObject()
object_Game2.object_texture("extras-32x-32.png", "picture", 32, 0, 32, 32, 1, 0, 0, 0)
object_Game2.random_position(map.map_list)

#Object 3
object_Game3 = GameObject()
object_Game3.object_texture("extras-32x-32.png", "picture", 64, 0, 32, 32, 1, 0, 0, 0)
object_Game3.random_position(map.map_list)


# Initialize game event
gameEvent = GameEvent()


pygame.display.flip()



# Main Loop Game
while game_running:
	for event in pygame.event.get():
		# Close game event
		if event.type==QUIT:
			game_running = 0			
		# Key control event	
		elif event.type == KEYDOWN:
			if event.key == K_UP:
				player.player_control("up", windows_screen,map.map_list)

			if event.key == K_DOWN:
				player.player_control("down", windows_screen, map.map_list)

			if event.key == K_LEFT:
				player.player_control("left", windows_screen, map.map_list)

			if event.key == K_RIGHT:
				player.player_control("right", windows_screen, map.map_list)
			
			# Take off the item when the player pick up it
			if (player.character_position_x, player.character_position_y) == (object_Game1.random_x, object_Game1.random_y):
				if object_Game1.object_state == 1:
					gameEvent.pickUp_object -= 1
				object_Game1.object_state = 0
				print(gameEvent.pickUp_object)

			if (player.character_position_x, player.character_position_y) == (object_Game2.random_x, object_Game2.random_y):
				if object_Game2.object_state == 1:
					gameEvent.pickUp_object -= 1
				object_Game2.object_state = 0
				print(gameEvent.pickUp_object)

			if (player.character_position_x, player.character_position_y) == (object_Game3.random_x, object_Game3.random_y):
				if object_Game3.object_state == 1:
					gameEvent.pickUp_object -= 1
				object_Game3.object_state = 0
				print(gameEvent.pickUp_object)


		

	# Updating of frame
	map.show_map(windows_screen)

	gameEvent.victory(gardian.character_proximity(player.character_position_x, player.character_position_y))
	if gameEvent.gardian_show == 1:
		gardian.show_character(windows_screen, 1)
	else:
		gardian.show_character(windows_screen, 0)
	if gameEvent.player_show == 1:
		player.show_character(windows_screen, 1)
	else:
		player.show_character(windows_screen, 0)

	object_Game1.show_object(windows_screen)
	object_Game2.show_object(windows_screen)
	object_Game3.show_object(windows_screen)
	pygame.display.flip()
	


