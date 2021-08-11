from os import path, walk, listdir
import shutil

progect_name = 'my_project_ok'

try:
    for root, dirs, files in walk(progect_name):
        if 'templates' in dirs and root != progect_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(progect_name, 'templates', entry))

except FileExistsError:
    print('Alredy worked with these templates!')
