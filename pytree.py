#!/usr/bin/env python3
import subprocess
import sys
import os
dirno=0
fileno=0

# YOUR CODE GOES here
def tree(pathname, indention):
    global dirno, fileno
    dirname, filename = os.path.split(pathname)
    print(indention+'├──', filename)
    if os.path.isdir(pathname):#if dir
        dirno+=1
        for list_item in os.listdir(pathname):
                #print(os.path.join(pathname, list_item))
                if not list_item.startswith('.'): tree(os.path.join(pathname, list_item),indention+"│  ")
    else:#if file
        fileno+=1

if __name__ == '__main__':
    print('.')
    if len(sys.argv)>= 2:
        for input_path in sys.argv[1:]:
            tree(input_path,'')
    else:
        tree(os.getcwd(),'')
    print(dirno,' directories, ',fileno,' files')
