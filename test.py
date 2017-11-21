level_design = []
GROUND_LIST = [] # List of coordinate X and Y of each ground texture
WALL_LIST = []
COOR_X = 0 # Cordinate X of the top left game zone
COOR_Y = 0
with open("LevelGame.txt", "r") as fichier:
	for ligne in fichier:
		for letter in ligne:
			if letter != "\n":
				level_design.append(letter)



x=1
for letter in level_design:
			
	if letter == "M":
		WALL_LIST.append((COOR_X, COOR_Y))
	elif letter == "S":
		GROUND_LIST.append((COOR_X, COOR_Y))
	COOR_X += 30
	if x == 15:			
		COOR_X = 0 # Back to begin
		COOR_Y += 30 # Moving to next line
		x=0
	x+=1



#print(level_design)
#print(WALL_LIST)
print(GROUND_LIST)
print(len(level_design))