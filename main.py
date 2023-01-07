
# Making a New Directory in Python using mkdir() method

# In Python, we can make a new directory using the mkdir() method.
# This method takes in the path of the new directory. If the full path is not specified, the new
# directory is created in the current working directory.

# Syntax : os.mkdir()

import os

current_dir = os.getcwd()

print(current_dir)  # Output : C:\work\python\Python\pythonDirectoryFiles

os.mkdir("text")

