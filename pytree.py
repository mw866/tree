#!/usr/bin/env python3
import subprocess
import sys
import os


# YOUR CODE GOES here
def tree(pathname, indention):
    dirname, filename = os.path.split(pathname)
    print(indention+'├──', filename)
    #if a dir
    if os.path.isdir(pathname):
            for list_item in os.listdir(pathname):
                    tree(os.path.join(dirname, list_item),indention+"│  ")

if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])
    print('.')
    if len(sys.argv)>= 2:
        for input_path in sys.argv[1:]:
            tree(input_path,'')
    else:
        tree(os.getcwd(),'')
