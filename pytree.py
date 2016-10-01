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
    print(indention, filename)
    if os.path.isdir(pathname):#if dir
        dirno += 1
        ls_items = os.listdir(pathname)
        for ls_item in ls_items:
            if not ls_item.startswith('.'):#if non-hidden
                if ls_item == ls_items[-1]:
                    new_indention = indention + '└──'
                else:
                    new_indention = indention + '├──'
                tree(os.path.join(pathname, ls_item), new_indention)
    else:#if file
        fileno += 1

if __name__ == '__main__':
    print('.')
    if len(sys.argv)>= 2:
        for input_path in sys.argv[1:]:
            tree(input_path,'')
    else:
        tree(os.getcwd(),'')
    print('\n',dirno,' directories, ',fileno,' files')
