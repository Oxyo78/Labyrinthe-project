#coding:utf-8
#! /usr/bin/env python3

""" import a texture, get the sprite position and size in the image, convert him to 30*30 pixel if they are not by default
	Attributes: File_name = name of the picture, must be a PNG (24 bits) format
				folder_name = Path folder of the picture
				pox_x_left_top and pos_t_left_top = Indicate the X and Y left top pixel position of the sprite (By default at X:0 and Y:0)
				size_x and size_y = Size in pixel of the picture (By default 30*30)
				alpha_sprite_file = Alpha filter image (by default it's no (0)) write : 1 for yes
				Red_color, green_color, blue_color = set the RGB color of the transparent color of your sprite ( By default it's black RGB(0, 0, 0))"""

from fonction.get_file import get_file_path
import pygame, os
from pygame.locals import *


def texture_for_sprite(file_name="", folder_file="", pos_x_left_top=0, pos_y_left_top=0, size_x=30, size_y=30, alpha_sprite_file=1, red_color=0, green_color=0, blue_color=0):
	try:
		# If the picture is an alpha filter image
		if alpha_sprite_file==0:
			texture = pygame.image.load(get_file_path(file_name, folder_file)).convert_alpha()	
			texture.set_clip(pygame.Rect(pos_x_left_top, pos_y_left_top, size_x, size_y))	
			texture_rect = texture.subsurface(texture.get_clip())
			texture_rect = pygame.transform.scale(texture,(30,30))
			print("0")
			return texture_rect

		# Not an alpha image
		else:
			texture = pygame.image.load(get_file_path(file_name, folder_file)).convert()	
			texture_rect = texture.subsurface(texture.get_clip())
			texture_rect = pygame.transform.scale(texture,(30,30))
			texture_rect.set_colorkey((red_color,green_color,blue_color))
			print("1")
			return texture_rect

	except:
		print("Error occured with the texture, need only a picture as PNG format (24 bits)")



def main():
	import fonction.map_generator
	map_lengh = fonction.map_generator.map_size("LevelGame.txt", "map")
	windows_screen = pygame.display.set_mode([int(map_lengh*30), int(map_lengh*30)])
	windows_screen.fill((100, 100, 100))

	image = texture_for_sprite(file_name="MacGyver.png", folder_file="Picture", size_x=32, size_y=43)
	windows_screen.blit(image, (30, 30))
	pygame.display.flip()

	game_running = 1
	while game_running:
		for event in pygame.event.get():
			# Close game event
			if event.type==QUIT:
				game_running = 0



if __name__ == "__main__":
	main()