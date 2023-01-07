
# Removing Directory or File using remove() and rmdir() method.

#  the remove() method or the rmdir() method to remove a file or directory.

# Syntax : os.remove("file_name") for removing the file
# Syntax : os.remove("dir_name") for removing the *empty* dir

import os

print("Before remove File : ", os.listdir())

os.remove("new_test.txt")   # remove the file new_test.txt

print("After remove file   : ", os.listdir())

os.rmdir("test_new")  # remove the dir test_new

print("After remove dir : ", os.listdir())

# Output :
# Before remove File :  ['.git', '.idea', 'main.py', 'new_test.txt', 'test_new', 'venv']
# After remove file   :  ['.git', '.idea', 'main.py', 'test_new', 'venv']
# After remove dir :  ['.git', '.idea', 'main.py', 'venv']