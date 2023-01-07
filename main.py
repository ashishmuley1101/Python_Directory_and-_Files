
# Changing Directory in Python

# changing the current working directory by using the chdir() method.
# The new path that we want to change into must be supplied as a string to this method.
# And we can use both the forward-slash / or the backward-slash \ to separate the path elements

# Syntax : os.chdir("new_dir_path")

import os

current_dir = os.getcwd()
print(current_dir)  # Output : C:\work\python\Python\pythonDirectoryFiles

os.chdir("C:\work\python\Python")
print(os.getcwd())  # Output : C:\work\python\Python

