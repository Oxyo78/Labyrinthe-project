#coding:utf-8
#! /usr/bin/env python3

"""Import a file from a folder"""

from os import path 

def get_file_path(data_file, folder):
	"""Get the path of the called file
	Syntax : get_file_path("name_of_file", "folder_of_file")"""

	try:
		directory = path.dirname(path.dirname(__file__))
		path_to_file = path.join(directory, folder, data_file)

		return path_to_file

		
	except FileNotFoundError as e:
		print("Loading error of the file : ", e)


def main():
	loading_file = get_file_path("LevelGame.txt", "map")

	with open(loading_file, "r") as file:
		preview = file.read()

		print(preview)



if __name__ == "__main__":
	main()