#coding:utf-8
#! /usr/bin/env python3

"""Class of the game"""

import pygame
from pygame.locals import *

import random
import time

from fonction.map_generator import map_size, map_initialize
from fonction.texture_loader import texture_for_sprite
from fonction.config import sprite_size


class LevelShow:
    """Loading and generator of the map from LevelGame.txt """

    def __init__(self):
        self.map_list = []
        self.player_pos = 0
        self.gardian_pos = 0


    def get_the_map_list(self):
        """Get the map list from file"""
        self.map_list = map_initialize("LevelGame.txt", "map")


    def show_map(self, windows_screen):
        """get texture of level et print"""
        ground = texture_for_sprite("floor-tiles-20x20.png", "picture", 160, 220, 20, 20, 0)
        wall = texture_for_sprite("floor-tiles-20x20.png", "picture", 60, 60, 20, 20, 0)
        finnish = texture_for_sprite("floor-tiles-20x20.png", "picture", 160, 20, 20, 20, 1)

        # Show the map on windows
        line_number = 0
        for line in self.map_list:
            case_number = 0
            for letter in line:
                if letter == "M": # print a wall sprite
                    windows_screen.blit(wall, (case_number*sprite_size, line_number*sprite_size))

                if letter == "G" or letter == "P" or letter == "B": # print a ground sprite
                    windows_screen.blit(ground, (case_number*sprite_size, line_number*sprite_size))

                    if letter == "P": # Get the pos of the player
                        self.player_pos = (case_number, line_number)

                    if letter == "B": # Get the pos of the gardian
                        self.gardian_pos = (case_number, line_number)

                if letter == "A": # print a finnish sprite on a ground sprite (transparent texture)
                    windows_screen.blit(ground, (case_number*sprite_size, line_number*sprite_size))
                    windows_screen.blit(finnish, (case_number*sprite_size, line_number*sprite_size))

                case_number += 1
            line_number += 1


class Character:
    """ initialize the character and control"""

    def __init__(self, charac_pos):
        """Get the position of the character from the map_list"""
        self.charac_pos_x, self.charac_pos_y = charac_pos
        # Get the size of the map in case
        self.lengh_map = map_size("LevelGame.txt", "map")
        self.charac_pos = 0


    def charac_texture(self, file, folder, pos_x, pos_y, size_x, size_y, alpha):
        """Get texture of player"""
        self.charac_texture = texture_for_sprite(file, folder, pos_x, pos_y, size_x, size_y, alpha)


    def dead_texture(self, file, folder, pos_x, pos_y, size_x, size_y, alpha):
        """Get the dead texture for body characer"""
        self.dead_texture = texture_for_sprite(file, folder, pos_x, pos_y, size_x, size_y, alpha)


    def show_charac(self, windows_screen, charac_is_alive):
        """Print the charace on map"""
        self.charac_pos = (self.charac_pos_x * sprite_size, self.charac_pos_y * sprite_size)
        if charac_is_alive == 1:
            windows_screen.blit(self.charac_texture, (self.charac_pos))
        else:
            windows_screen.blit(self.dead_texture, (self.charac_pos))


    def player_control(self, direction, windows_screen, map_list):
        """Control the direction of the character wih keyboard Up, Down, Left, Right"""
        if  direction == "up":
            if self.charac_pos_y != 0: # Border up windows check
                if map_list[self.charac_pos_y - 1][self.charac_pos_x] != "M": # Wall collision check
                    self.charac_pos_y -= 1 # Go up of 1 case

        if direction == "down":
            if self.charac_pos_y != self.lengh_map -1: # Border down windows check
                if map_list[self.charac_pos_y + 1][self.charac_pos_x] != "M": # Wall collision check
                    self.charac_pos_y += 1 # Go down of 1 case

        if direction == "right":
            if self.charac_pos_x != self.lengh_map - 1: # Border right windows check
                if map_list[self.charac_pos_y][self.charac_pos_x + 1] != "M": # Wall collision check
                    self.charac_pos_x += 1 # Go right of 1 case

        if direction == "left":
            if self.charac_pos_x != 0: # Border left windows check
                if map_list[self.charac_pos_y][self.charac_pos_x - 1] != "M": # Wall collision check
                    self.charac_pos_x -= 1 # go left of 1 case

    def charac_proximity(self, player_pos_x, player_pos_y):
        """Proximity detection between player and other character"""

        if (player_pos_x, player_pos_y) == (self.charac_pos_x -1, self.charac_pos_y):
            return 1
        elif (player_pos_x, player_pos_y) == (self.charac_pos_x +1, self.charac_pos_y):
            return 1
        elif (player_pos_x, player_pos_y) == (self.charac_pos_x, self.charac_pos_y -1):
            return 1
        elif (player_pos_x, player_pos_y) == (self.charac_pos_x, self.charac_pos_y +1):
            return 1


class GameObject:
    """ Initialize an game object """

    count_object = 0 # Add 1 for each object created

    def __init__(self):
        self.random_y = 0
        self.random_x = 0
        self.object_state = 1
        GameObject.count_object += 1


    def object_texture(self, file, folder, pos_x, pos_y, size_x, size_y, alpha):
        """Get the texture of the object to show"""
        self.texture = texture_for_sprite(file, folder, pos_x, pos_y, size_x, size_y, alpha)


    def random_pos(self, map_list):
        """Get a random position in the level list on ground position"""
        self.random_loop = True
        self.random_y = 0
        self.random_x = 0

        while self.random_loop:
            """get a random pos for the oject"""
            self.random_y = random.randrange(0, 14)
            self.random_x = random.randrange(0, 14)
            if map_list[self.random_y][self.random_x] != "M":
                if map_list[self.random_y][self.random_x] != "B":
                    if map_list[self.random_y][self.random_x] != "P":
                        break
            else:
                continue

    def show_object(self, windows_screen):
        """Show the item with the random pos"""
        if self.object_state == 1: # if the item is no pick up, show him
            windows_screen.blit(self.texture, (self.random_x * 30, self.random_y * 30))



class GameEvent:
    """Game event"""
    def __init__(self):
        self.pickup_object = GameObject.count_object
        self.game_end = 1
        self.gardian_show = 1
        self.player_show = 1
        self.final_text = 0
        self.text = ""

    def victory(self, proximity_detection):
        """Victory or defeat"""
        if proximity_detection == 1:
            if self.pickup_object == 0:
                self.gardian_show = 0
            else:
                self.player_show = 0
            self.game_end = 0

    def text_game(self, windows_screen, number_text):
        """print the text on screen game"""
        if number_text == 1:
            self.font = pygame.font.SysFont("calibri", 20)
            self.text = self.font.render("Pick up the 3 items to fight the gardian", True, (255, 255, 10))
            windows_screen.blit(self.text, (20, 460))

        if number_text == 2:           
            if self.pickup_object == 0:
                windows_screen.fill((0, 0, 0))
                self.font = pygame.font.SysFont("calibri", 20)
                self.text = self.font.render("We got the 3 items, let's fight the gardian !", True, (255, 255, 10))
                windows_screen.blit(self.text, (20, 460))

        if number_text == 3:
            self.font = pygame.font.SysFont("calibri", 50)
            self.text_to_print = self.font.render("GAME OVER", False, (255, 255, 10))
            windows_screen.blit(self.text_to_print, (100, 50))

            if self.gardian_show == 1:
                self.font = pygame.font.SysFont("calibri", 30)
                self.text_to_print = self.font.render("You lose...", True, (255, 255, 30))
                windows_screen.blit(self.text_to_print, (170, 110))

            if self.player_show == 1:
                self.font = pygame.font.SysFont("calibri", 30)
                self.text_to_print = self.font.render("You escape ! Yahouuuuu", True, (255, 255, 30))
                windows_screen.blit(self.text_to_print, (75, 110))
