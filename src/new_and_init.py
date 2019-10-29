"""
The difference between __new__ and __init__ method in a class.

__new__ is used to create an instance of the class and
it is called each time a new instance is created.
__new__() method must return a value, an object which is the common case.

__init__ is an initiator, it is called after an instance is created already.
"""


class Foo:
    def __new__(cls, *args, **kwargs):
        print('__new__() method is called.')
        return super(Foo, cls).__new__(cls)

    def __init__(self):
        print('__init__() method is called.')
        self.member = 'member variable of ' + self.__class__.__name__

    def __get__(self, instance, owner):
        return self.member


def main():
    foo = Foo()
    print(foo.member)


if __name__ == '__main__':
    main()
