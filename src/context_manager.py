"""
A context manager can simplify usage in resource
allocate and de-allocate routines along with the 'with' keyword.

A context manager in Python is an object that implements
__enter__(self) and __exit__(self, type, value, traceback) methods.

The most common context manager looks like this:

with open('demo.txt', 'w') as f_obj:
    f_obj.write('foo')

Comments from the official site:
https://book.pythontips.com/en/latest/context_managers.html

say that:

Context managers allow you to allocate and release resources precisely when you want to.
The most widely used example of context managers is the with statement.
Suppose you have two related operations which you’d like to execute as a pair,
with a block of code in between. Context managers allow you to do specifically that.
"""


# Now let's define out own context manager.
class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.name, self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


def main():
    name = 'demo.txt'
    with File(name, 'w') as f_obj:
        f_obj.write('foo\n')
        f_obj.write('bar\n')

    # Best practice to read a file.
    print('read the file into a list.')
    with File(name, 'r') as f_obj:
        lines = f_obj.readlines()
        print(type(lines))
        for line in lines:
            print(line.strip())
    # Not recommending practice.
    print('read the file one line at a time.')
    with File(name, 'r') as f_obj:
        while True:
            line = f_obj.readline()
            if line:
                print(line.strip())
            else:
                break
    # Not recommending practice.
    print('read the whole file all in once.')
    with File(name, 'r') as f_obj:
        print(f_obj.read())


if __name__ == '__main__':
    main()
