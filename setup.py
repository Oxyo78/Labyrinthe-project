"""Setup file to create a exe"""

from cx_Freeze import setup, Executable

# call setup  and add files / folder
setup(
    name = "Save MacGyver !",
    version = "1.00",
    options= {"build_exe": {"packages": ["pygame"],
                            "include_files": ["class_game.py", "map", "picture", "fonction"]}},		
    description = "OC-Project 3 by Yohan V",
    executables = [Executable("main.py")],
)