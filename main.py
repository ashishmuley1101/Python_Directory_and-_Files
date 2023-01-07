
# Renaming a Directory  and File using rename() method.

# The rename() method can rename a directory or a file.
# For renaming any directory or file, rename() takes in two basic arguments:
# the old name as the first argument
# the new name as the second argument.

# Syntax : os.rename("old_name", "new_name")

import os

print(os.listdir())  # Output : ['.git', '.idea', 'main.py', 'test.txt', 'text', 'venv']

os.rename("text", "test_new")   # rename the dir text to test_new dir

print(os.listdir())  # Output : ['.git', '.idea', 'main.py', 'test.txt', 'test_new', 'venv']

with open("test.txt", "w") as file:
    file.write("This is test for rename.")

os.rename("test.txt", "new_test.txt")  # rename the file test.txt to new_test.txt

print(os.listdir())  # Output : ['.git', '.idea', 'main.py', 'new_test.txt', 'test_new', 'venv']


