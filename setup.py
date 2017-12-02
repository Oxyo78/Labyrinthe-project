"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Save MacGyver !",
    version = "1.00",
    options= {"build_exe": {"packages": ["pygame"]}},
    description = "OC-Project 3 by Yohan V",
    executables = [Executable("main.py")],
)