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

#Get texture and scale 30*30
ground_texture = pygame.image.load("Picture/floor-tiles-20x20.png").convert()
wall_texture = pygame.image.load("Picture/floor-tiles-20x20.png").convert()
ground_texture.set_clip(pygame.Rect(160, 220, 20, 20))
wall_texture.set_clip(pygame.Rect(40, 60, 20, 20))
ground = ground_texture.subsurface(ground_texture.get_clip())
wall = wall_texture.subsurface(wall_texture.get_clip())
ground = pygame.transform.scale(ground,(30,30)) # Convertion of the sprit 20*20 in 30*30 pixels
wall = pygame.transform.scale(wall,(30,30)) # Convertion of the sprit 20*20 in 30*30 pixels


# Pick up the both list from the Class LevelGenerator
map = LevelGenerator()
coor_wall, coor_ground = map.map_generator()
for x,y in coor_ground:
	windows_screen.blit(ground, (x, y))
	print(x, y)
for x,y in coor_wall:
	windows_screen.blit(wall, (x, y))

#Affiche les coordonnée des mur
#print(coor_ground)

pygame.display.flip()


while game_running:
	for event in pygame.event.get():
			#pygame prend le premier évènement de la file
			if event.type==QUIT:
			#l'évènement QUIT correspond au clic sur la croix
				game_running = 0
