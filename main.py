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


pygame.display.flip()


while game_running:
	for event in pygame.event.get():
			# Close game event
			if event.type==QUIT:
				game_running = 0
			
			# Key control event	
			elif event.type == KEYDOWN:
				if event.key == K_UP:
					player.mouvement("up", windows_screen, map.level_design)

				if event.key == K_DOWN:
					player.mouvement("down", windows_screen, map)

				if event.key == K_LEFT:
					player.mouvement("left", windows_screen, map)

				if event.key == K_RIGHT:
					player.mouvement("right", windows_screen, map)

	map.affichage(windows_screen)
	gardien.characterPosition(windows_screen)

