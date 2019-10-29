"""
Given a path, list all files in the path recursively.
precede directories with hyphen '--',
precede regular files with asterisks '**'.
"""
from os import listdir, walk
from os.path import join, isdir, exists


# Solution 1, use walk.
def walk_dir(directory):
    for root, dirs, files in walk(directory):
        print(root)
        for d in dirs:
            print('--', d)
        for f in files:
            print('**', f)


# Solution 2, use listdir recursively.
def list_recursive(directory):
    if exists(directory):
        print('--', directory)
    else:
        print('directory %s does not exist!', directory)
    for child in listdir(directory):
        tmp = join(directory, child)
        if isdir(tmp):
            print('--', tmp)
            list_recursive(tmp)  # here is a recursion.
        else:
            print('**', tmp)


def main():
    walk_dir('.')
    print('--------------')
    list_recursive('..')


if __name__ == '__main__':
    main()
