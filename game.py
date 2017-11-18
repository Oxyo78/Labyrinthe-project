#Importation des modules
import pygame, os
from pygame.locals import *
import Fonction

#Déclaration de la longueur de la fenetre
SCREEN_WIDTH=640
SCREEN_HEIGHT=480

#Declaration des variables
game_running = True

#Création de la fenetre
screen_game = Fonction.screen(SCREEN_WIDTH, SCREEN_HEIGHT)

#Chargment de la texture de fond
Fonction.background(screen_game)

pygame.display.flip()

while game_running:
	game_running=int(input())
	continue
