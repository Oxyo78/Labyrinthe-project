import Class_game
import pygame
from pygame.locals import *

game_running = True
SCREEN_WIDTH=640
SCREEN_HEIGHT=470

affichage = Class_game.Game_motor(SCREEN_WIDTH, SCREEN_HEIGHT)


while game_running:
	for event in pygame.event.get():
			#pygame prend le premier évènement de la file
			if event.type==QUIT:
			#l'évènement QUIT correspond au clic sur la croix
				game_running = 0
