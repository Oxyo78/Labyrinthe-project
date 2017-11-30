#coding:utf-8
#! /usr/bin/env python3

""" Contains the function to get the size map(map_size) and map generator(map_initialize) """

from fonction.get_file import get_file_path
from config import *



def map_size(file_to_open, folder_file):
	""" Get the size of the map for pygame windows size"""

	# loading of the file as "file"
	loading_file = get_file_path(file_to_open, folder_file)

	with open(loading_file, "r") as file:
		# Reading each line
		for line in file:
			# delete the \n characters at the end of line
			lengh_map = line.rstrip("\n")

	return len(lengh_map)*sprite_size




def map_initialize(file_to_open, folder_file):
	try:
		loading_file = get_file_path(file_to_open, folder_file)

		with open(loading_file, "r") as file:
			mapping = [] 
			# Reading each line
			for line in file:
				# delete the \n characters at the end of line
				line = line.rstrip("\n")
				Line_list = []
				# Read each letter in line
				for letter in line:
					Line_list.append(letter)
				# Add each line to mapping list
				mapping.append(Line_list)

			return mapping
					
	except:
		print("Error occured during the map generator, please check the file.txt")

		

def main():
	# Control of the mapping by print the DF list on console
	import pandas as pd
	map_list_df = pd.DataFrame(map_initialize("LevelGame.txt", "map"))
	print(map_list_df)


if __name__ == "__main__":
	main()