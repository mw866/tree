#!/usr/bin/env python3
import subprocess
import sys
import os
dirno = 0
fileno = 0

# YOUR CODE GOES here
def tree(pathname, isLast_list):
    global dirno, fileno
    dirname, filename = os.path.split(pathname)
    prefix= ''
    for isLast in isLast_list[:-1]:
        if isLast==True:
            prefix += '   '#('└──')
        else:
            prefix += '│  ' #('├──')
    if isLast_list[-1]==True:
        prefix += ('└──')
    else:
        prefix += ('├──')
    print(prefix, filename)

    if os.path.isdir(pathname):  #for dir
        dirno += 1
        ls_items = os.listdir(pathname)
        for ls_item in ls_items:
            if not ls_item.startswith('.'):  #if non-hidden
                if ls_item == ls_items[-1]:
                    tree(os.path.join(pathname, ls_item), isLast_list+[True])
                else:
                    tree(os.path.join(pathname, ls_item), isLast_list+[False])
    else:  #for file
        fileno += 1

# def init(pathname, isLast_list):
    # ls_items = os.listdir(pathname)
    # for ls_item in ls_items:
    #         if not ls_item.startswith('.'):  #if non-hidden
    #             if ls_item == ls_items[-1]:
    #                 #new_isLast_list = isLast_list + ['└──']
    #                 isLast = True
    #             else:
    #                 #new_isLast_list = isLast_list + ['├──']
    #                 isLast = False
    #             tree(os.path.join(pathname, ls_item), isLast_list, isLast)

# def init_todelete(pathname, isLast_list):
#     for root, dirs, files in os.walk(pathname):
#             print(files)

if __name__ == '__main__':
    print('.')
    if len(sys.argv)>= 2:
        for input_path in sys.argv[1:]:
            tree(input_path, [True, True])
    else:
        tree(os.getcwd(), [True, True])
    print('\n')
    print(dirno, 'directories,', fileno, 'files')
