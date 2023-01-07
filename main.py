
# Removing non-empty Directory in python using shutil module rmtree() method.


# Syntax : os.rmtres("dir_name") for removing the *empty* dir

import os
import shutil

os.mkdir("dir_new") # creating the dir_name dir

print("Dir and Files : ", os.listdir())

os.chdir("C:\work\python\Python\pythonDirectoryFiles\dir_new")   # changing the current dir_name dir

with open("test.txt", "w") as file:   # creating the test.txt file inside the current dir
    file.write("Hello from bridgelabz.!")

os.chdir("C:\work\python\Python\pythonDirectoryFiles")  # changing the current dir to older dir

print("Dir and Files   : ", os.listdir())

shutil.rmtree("dir_new")  # remove the dir test_new which is non-empty dir

print("After remove dir : ", os.listdir())

# Output :
# Dir and Files :  ['.git', '.idea', 'dir_new', 'main.py', 'venv']
# Dir and Files   :  ['.git', '.idea', 'dir_new', 'main.py', 'venv']
# After remove dir :  ['.git', '.idea', 'main.py', 'venv']