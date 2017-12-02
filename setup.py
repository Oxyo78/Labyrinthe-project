"""Setup file to create a exe"""

import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:/Python363/tcl/tcl8.6"
os.environ['TK_LIBRARY'] = "C:/Python363/tcl/tk8.6"


# call setup  and add files / folder
setup(
    name = "Save MacGyver !",
    version = "1.00",
    options= {"build_exe": {"packages": ["pygame"],
                            "include_files": ["class_game.py", "map", "picture", "fonction"]}},		
    description = "OC-Project 3 by Yohan V",
    executables = [Executable("main.py")],
)