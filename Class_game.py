import pygame, os
from pygame.locals import *

class LevelGenerator:
	"""Loading and generator of the map from LevelGame.txt """
	LEVEL_DESIGN = [] #List of the letter in file
	GROUND_LIST = [] # List of coordinate X and Y of each ground texture
	WALL_LIST = [] # List of coordinate X and Y of each wall texture, It's use for collision.mouvement.player


	def __init__(self):
		with open("LevelGame.txt", "r") as fichier:
			for ligne in fichier:
				for letter in ligne:
					self.LEVEL_DESIGN.append(letter)

	
	def map_generator(self):
		COOR_X = 0 # Cordinate X of the top left game zone
		COOR_Y = 0 # Cordinate Y of the top left game zone

		count_line = 0# Count the number of sprite by line (15)
		for letter in self.LEVEL_DESIGN:
			if letter == "M":
				self.WALL_LIST.append((COOR_X, COOR_Y))
			elif letter == "S":
				self.GROUND_LIST.append((COOR_X, COOR_Y))
			COOR_X += 30
			if count_line == 15: # If he is at the end of line (15 sprite)		
				COOR_X = 0 # Back to begin
				COOR_Y += 30 # Moving to next line
				count_line = 0 # And restart
			count_line += 1

		return self.WALL_LIST, self.GROUND_LIST



m = LevelGenerator()
w, g = m.map_generator()
print(g)

		



	#def rafraichissement_ecran(self,affichage):
		
class ObjectMap:
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y
	pass

class Player(ObjectMap):
#	def __init__(self, x, y):
#		super(x, y)

	def move():
		pass

class Gardien:
	pass


#mcgyver = Player(3, 4)
#tube = ObjectMap(4, 5)
#guardien = ObjectMap(6, 7)

#mcgyver.x == 3
#mcgyver.y == 4

#mcgyver.move(4,5)
#tube.move(!!!!)

#if mcgyver == guardien:
#	victoire()

#if mcgyver == tube:
#	mcgyver>ramasser(tube)

