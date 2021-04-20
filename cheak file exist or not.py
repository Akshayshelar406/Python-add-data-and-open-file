import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("File not exist")