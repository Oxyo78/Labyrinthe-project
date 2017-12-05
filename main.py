#coding:utf-8
#! /usr/bin/env python3

"""Main file of the game
    Poject 3 - OpenclassRooms by Yohan V"""


import pygame
from pygame.locals import *

from class_game import LevelShow, Character, GameObject, GameEvent
from fonction.map_generator import map_size
from fonction.config import *

#initialize pygame
pygame.init()

# Variable
game_running = 1 # loop game

# Get the size of the screen from the file map
LENGH_SCREEN = map_size("LevelGame.txt", "map")

# initialize the windows, name and keydown loop
lengh_screen = int(LENGH_SCREEN)*sprite_size
windows_screen = pygame.display.set_mode([lengh_screen, lengh_screen + 50])
pygame.display.set_caption("Save Macgyver !")
pygame.key.set_repeat(400, 30)

# Print the level on windows
level = LevelShow()
level.get_the_map_list()
level.show_map(windows_screen)

# Initialise the player class
player = Character(level.player_pos)
player.charac_texture("Macgyver.png", "picture", 0, 0, 32, 43, 1)
player.dead_texture("extras-32x-32.png", "picture", 192, 0, 32, 32, 1)

# Initialize the gardian class
gardian = Character(level.gardian_pos)
gardian.charac_texture("Gardien.png", "picture", 0, 0, 32, 36, 1)
gardian.dead_texture("extras-32x-32.png", "picture", 192, 0, 32, 32, 1)

#Object 1
object_Game1 = GameObject()
object_Game1.object_texture("extras-32x-32.png", "picture", 0, 0, 32, 32, 1)
object_Game1.random_pos(level.map_list)

#Object 2
object_Game2 = GameObject()
object_Game2.object_texture("extras-32x-32.png", "picture", 32, 0, 32, 32, 1)
object_Game2.random_pos(level.map_list)

#Object 3
object_Game3 = GameObject()
object_Game3.object_texture("extras-32x-32.png", "picture", 64, 0, 32, 32, 1)
object_Game3.random_pos(level.map_list)


# Initialize game event
gameEvent = GameEvent()
pygame.display.flip()
gameEvent.text_game(windows_screen, 1)


# Main Loop Game
while game_running:
    for event in pygame.event.get():
		# Close game event
        if event.type == QUIT:
            game_running = 0
		# Key control event
        elif event.type == KEYDOWN:
            if gameEvent.game_end == 1:
                if event.key == K_UP:
                    player.player_control("up", windows_screen, level.map_list)

                if event.key == K_DOWN:
                    player.player_control("down", windows_screen, level.map_list)

                if event.key == K_LEFT:
                    player.player_control("left", windows_screen, level.map_list)

                if event.key == K_RIGHT:
                    player.player_control("right", windows_screen, level.map_list)

				# Take off item when the player pick up it
                new_player_position = player.charac_pos_x, player.charac_pos_y
                if new_player_position == (object_Game1.random_x, object_Game1.random_y):
                    if object_Game1.object_state == 1:
                        gameEvent.pickup_object -= 1
                        gameEvent.text_game(windows_screen, 2)
                    object_Game1.object_state = 0

                if new_player_position == (object_Game2.random_x, object_Game2.random_y):
                    if object_Game2.object_state == 1:
                        gameEvent.pickup_object -= 1
                        gameEvent.text_game(windows_screen, 2)
                    object_Game2.object_state = 0

                if new_player_position == (object_Game3.random_x, object_Game3.random_y):
                    if object_Game3.object_state == 1:
                        gameEvent.pickup_object -= 1
                        gameEvent.text_game(windows_screen, 2)                   
                    object_Game3.object_state = 0


	# Updating frame
    level.show_map(windows_screen)

    # player proximity of gardian
    PLAYER_POSITION_X = player.charac_pos_x
    PLAYER_POSITION_Y = player.charac_pos_y
    gameEvent.victory(gardian.charac_proximity(PLAYER_POSITION_X, PLAYER_POSITION_Y))

    # If player lose
    if gameEvent.gardian_show == 1:
        gardian.show_charac(windows_screen, 1)
    else:
        gardian.show_charac(windows_screen, 0)
        gameEvent.text_game(windows_screen, 3)
    # If player win
    if gameEvent.player_show == 1:
        player.show_charac(windows_screen, 1)   
    else:
        player.show_charac(windows_screen, 0)
        gameEvent.text_game(windows_screen, 3)

    object_Game1.show_object(windows_screen)
    object_Game2.show_object(windows_screen)
    object_Game3.show_object(windows_screen)
    pygame.display.flip()
