import os
import fnmatch


def find_music(start, extension):
    for path, directiories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(path, file)


for f in find_music('music', 'emp3'):
    print(f)