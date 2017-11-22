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

pygame.display.flip()


while game_running:
	for event in pygame.event.get():
			#pygame prend le premier évènement de la file
			if event.type==QUIT:
			#l'évènement QUIT correspond au clic sur la croix
				game_running = 0

