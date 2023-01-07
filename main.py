
# List Directories and Files in Python using listdir()

# All files and sub-directories inside a directory can be retrieved using the listdir() method.
# This method takes in a path and returns a list of subdirectories and files in that path.
# If no path is specified, it returns the list of subdirectories and files from the current working directory.

# Syntax : os.listdir()

import os

current_dir = os.getcwd()

print(current_dir)  # Output : C:\work\python\Python\pythonDirectoryFiles

print(os.listdir())  # Output : ['.git', '.idea', 'main.py', 'venv']

print(os.listdir("C:\\"))
# returning all the dir and sub-dir from the drive in specified path in list data type.
