#!/usr/bin/env python3
import subprocess
import sys
import os
import locale
locale.setlocale(locale.LC_ALL, '')
dirno = 0
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
        recurse(pathname, isLast_list)
    else:  # for file
        fileno += 1


def recurse(pathname, isLast_list):
    ls_items = [ls_item for ls_item in sorted(os.listdir(pathname), key=locale.strxfrm) if not ls_item.startswith('.')]

    for ls_item in ls_items:
        if ls_item == ls_items[-1]:
            tree(os.path.join(pathname, ls_item), isLast_list + [True])
        else:
            tree(os.path.join(pathname, ls_item), isLast_list + [False])


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        for input_path in sys.argv[1:]:
            print(input_path)
            recurse(input_path, [])
    else:
        print('.')
        recurse(os.getcwd(), [])
    print('')
    print(dirno, 'directories,', fileno, 'files')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
