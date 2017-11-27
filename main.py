#coding:utf-8

from Class_game import *
import pygame, os
from pygame.locals import *

#Variables
game_running = True
screen_width=640
screen_height=470


windows_screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Sauvez MacGyver !")
pygame.key.set_repeat(400,30) 

map = LevelGenerator()
map.map_generator()
map.affichage(windows_screen)

player = Character("Picture/MacGyver.png", 280, 400)
player.characterPosition(windows_screen)

gardien = Character("Picture/Gardien.png", 400, 190)
gardien.characterPosition(windows_screen)
map.wall_pos.append((gardien.pos_x, gardien.pos_y)) # Bug ? ne s'ajoute pas a la liste de l'event KEYDOWN
#print(map.wall_pos)

#Object 1
Object_Game1 = ItemMap("Picture/extras-32x-32.png")
Object_Game1.random_position(map.ground_pos)
Object_Game1.affichageObject(0, 0, 0, windows_screen)

#Object 2
Object_Game2 = ItemMap("Picture/extras-32x-32.png")
Object_Game2.random_position(map.ground_pos)
Object_Game2.affichageObject(32, 0, 1, windows_screen)

#Object 3
Object_Game3 = ItemMap("Picture/extras-32x-32.png")
Object_Game3.random_position(map.ground_pos)
Object_Game3.affichageObject(64, 0, 2, windows_screen)

pygame.display.flip()




while game_running:
	for event in pygame.event.get():
		# Close game event
		if event.type==QUIT:
			game_running = 0			
		# Key control event	
		elif event.type == KEYDOWN:
			if event.key == K_UP:
				player.mouvement("up", windows_screen, map.wall_pos)

			if event.key == K_DOWN:
				player.mouvement("down", windows_screen, map.wall_pos)

			if event.key == K_LEFT:
				player.mouvement("left", windows_screen, map.wall_pos)

			if event.key == K_RIGHT:
				player.mouvement("right", windows_screen, map.wall_pos)
			Object_Game1.affichageObject(0, 0, 0, windows_screen)
			Object_Game2.affichageObject(32, 0, 1, windows_screen)
			Object_Game3.affichageObject(64, 0, 2, windows_screen)
	map.affichage(windows_screen)
	gardien.characterPosition(windows_screen)
	


