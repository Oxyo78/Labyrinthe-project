#Importation des modules
import pygame, os
from pygame.locals import *
import Fonction

#Déclaration de la longueur de la fenetre
SCREEN_WIDTH=640
SCREEN_HEIGHT=470

#Declaration des variables
game_running = True

#Création de la fenetre
screen_game = Fonction.screen(SCREEN_WIDTH, SCREEN_HEIGHT)

#Chargment de la texture de fond
Fonction.background(screen_game)

#Affichage du joueur
Fonction.player(screen_game)
Fonction.gardien(screen_game)
pygame.display.flip()

while game_running:
	for event in pygame.event.get():
		#pygame prend le premier évènement de la file
		if event.type==QUIT:
			#l'évènement QUIT correspond au clic sur la croix
			game_running = 0
			#permet de quitter la boucle 
