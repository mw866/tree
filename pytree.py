#!/usr/bin/env python3
import subprocess
import sys
import os
import locale
dirno = 0
# locale.setlocale(locale.LC_ALL, 'en_US.utf8')
fileno = 0


# YOUR CODE GOES here
def tree(pathname, isLast_list):
    global dirno, fileno
    dirname, filename = os.path.split(pathname)
    prefix = ''
    for isLast in isLast_list[:-1]:
        if isLast:
            prefix += '    '
        else:
            prefix += '│   '
    if isLast_list[-1]:
        prefix += ('└──')
    else:
        prefix += ('├──')
    print(prefix, filename)

    if os.path.isdir(pathname):  # for dir
        dirno += 1
        ls_items = sorted(os.listdir(pathname), key=str.upper)
        for ls_item in ls_items:
            if not ls_item.startswith('.'):  # if non-hidden
                if ls_item == ls_items[-1]:
                    tree(os.path.join(pathname, ls_item), isLast_list + [True])
                else:
                    tree(os.path.join(pathname, ls_item), isLast_list + [False])
    else:  # for file
        fileno += 1


def root(pathname, isLast_list):
    ls_items = sorted(os.listdir(pathname), key=str.upper)
    for ls_item in ls_items:
        if not ls_item.startswith('.'):  # if non-hidden
            if ls_item == ls_items[-1]:
                tree(os.path.join(pathname, ls_item), isLast_list + [True])
            else:
                tree(os.path.join(pathname, ls_item), isLast_list + [False])

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        for input_path in sys.argv[1:]:
            print(input_path)
            root(input_path, [])
    else:
        print('.')
        root(os.getcwd(), [])
    print('')
    print(dirno, 'directories,', fileno, 'files')
