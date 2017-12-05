#coding:utf-8
#! /usr/bin/env python3

"""Main file of the game
    Poject 3 - OpenclassRooms by Yohan V"""


import pygame
from pygame.locals import QUIT
from pygame.locals import KEYDOWN
from pygame.locals import K_RIGHT
from pygame.locals import K_LEFT
from pygame.locals import K_DOWN
from pygame.locals import K_UP

from class_game import LevelShow, Character, GameObject, GameEvent
from fonction.map_generator import map_size
from fonction.config import SPRITE_SIZE

#initialize pygame
pygame.init()

# Variable
GAME_RUNNING = 1 # loop game

# Get the size of the screen from the file map
LENGH_SCREEN = map_size("LevelGame.txt", "map")

# initialize the windows, name and keydown loop
LENGH_SCREEN = int(LENGH_SCREEN)*SPRITE_SIZE
WNDOWS_SCREEN = pygame.display.set_mode([LENGH_SCREEN, LENGH_SCREEN + 50])
pygame.display.set_caption("Save Macgyver !")
pygame.key.set_repeat(400, 30)

# Print the LEVEL on windows
LEVEL = LevelShow()
LEVEL.get_the_map_list()
LEVEL.show_map(WNDOWS_SCREEN)

# Initialise the PLAYER class
PLAYER = Character(LEVEL.player_pos)
PLAYER.charac_texture("Macgyver.png", "picture", 0, 0, 32, 43, 1)
PLAYER.dead_texture("extras-32x-32.png", "picture", 192, 0, 32, 32, 1)

# Initialize the GARDIAN class
GARDIAN = Character(LEVEL.gardian_pos)
GARDIAN.charac_texture("Gardien.png", "picture", 0, 0, 32, 36, 1)
GARDIAN.dead_texture("extras-32x-32.png", "picture", 192, 0, 32, 32, 1)

#Object 1
OBJECT_GAME1 = GameObject()
OBJECT_GAME1.object_texture("extras-32x-32.png", "picture", 0, 0, 32, 32, 1)
OBJECT_GAME1.random_pos(LEVEL.map_list)

#Object 2
OBJECT_GAME2 = GameObject()
OBJECT_GAME2.object_texture("extras-32x-32.png", "picture", 32, 0, 32, 32, 1)
OBJECT_GAME2.random_pos(LEVEL.map_list)

#Object 3
OBJECT_GAME3 = GameObject()
OBJECT_GAME3.object_texture("extras-32x-32.png", "picture", 64, 0, 32, 32, 1)
OBJECT_GAME3.random_pos(LEVEL.map_list)


# Initialize game event
GAMEEVENT = GameEvent()
pygame.display.flip()
GAMEEVENT.text_game(WNDOWS_SCREEN, 1)


# Main Loop Game
while GAME_RUNNING:
    for event in pygame.event.get():
		# Close game event
        if event.type == QUIT:
            GAME_RUNNING = 0
		# Key control event
        elif event.type == KEYDOWN:
            if GAMEEVENT.game_end == 1:
                if event.key == K_UP:
                    PLAYER.player_control("up", LEVEL.map_list)

                if event.key == K_DOWN:
                    PLAYER.player_control("down", LEVEL.map_list)

                if event.key == K_LEFT:
                    PLAYER.player_control("left", LEVEL.map_list)

                if event.key == K_RIGHT:
                    PLAYER.player_control("right", LEVEL.map_list)

				# Take off item when the PLAYER pick up it
                new_player_position = PLAYER.charac_pos_x, PLAYER.charac_pos_y
                if new_player_position == (OBJECT_GAME1.random_x, OBJECT_GAME1.random_y):
                    if OBJECT_GAME1.object_state == 1:
                        GAMEEVENT.pickup_object -= 1
                        GAMEEVENT.text_game(WNDOWS_SCREEN, 2)
                    OBJECT_GAME1.object_state = 0

                if new_player_position == (OBJECT_GAME2.random_x, OBJECT_GAME2.random_y):
                    if OBJECT_GAME2.object_state == 1:
                        GAMEEVENT.pickup_object -= 1
                        GAMEEVENT.text_game(WNDOWS_SCREEN, 2)
                    OBJECT_GAME2.object_state = 0

                if new_player_position == (OBJECT_GAME3.random_x, OBJECT_GAME3.random_y):
                    if OBJECT_GAME3.object_state == 1:
                        GAMEEVENT.pickup_object -= 1
                        GAMEEVENT.text_game(WNDOWS_SCREEN, 2)
                    OBJECT_GAME3.object_state = 0


	# Updating frame
    LEVEL.show_map(WNDOWS_SCREEN)

    # PLAYER proximity of GARDIAN
    PLAYER_POSITION_X = PLAYER.charac_pos_x
    PLAYER_POSITION_Y = PLAYER.charac_pos_y
    GAMEEVENT.victory(GARDIAN.charac_proximity(PLAYER_POSITION_X, PLAYER_POSITION_Y))

    # If PLAYER lose
    if GAMEEVENT.gardian_show == 1:
        GARDIAN.show_charac(WNDOWS_SCREEN, 1)
    else:
        GARDIAN.show_charac(WNDOWS_SCREEN, 0)
        GAMEEVENT.text_game(WNDOWS_SCREEN, 3)
    # If PLAYER win
    if GAMEEVENT.player_show == 1:
        PLAYER.show_charac(WNDOWS_SCREEN, 1)
    else:
        PLAYER.show_charac(WNDOWS_SCREEN, 0)
        GAMEEVENT.text_game(WNDOWS_SCREEN, 3)

    OBJECT_GAME1.show_object(WNDOWS_SCREEN)
    OBJECT_GAME2.show_object(WNDOWS_SCREEN)
    OBJECT_GAME3.show_object(WNDOWS_SCREEN)
    pygame.display.flip()
