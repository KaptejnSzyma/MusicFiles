import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    print(directories)
    print(files)
    input()