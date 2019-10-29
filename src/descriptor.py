"""
Descriptor definition from official site:
https://docs.python.org/3/howto/descriptor.html

say that:
In general, a descriptor is an object attribute with “binding behavior”,
one whose attribute access has been overridden by methods in the descriptor protocol.
Those methods are __get__(), __set__(), and __delete__().
If any of those methods are defined for an object, it is said to be a descriptor.
"""


# Define our own descriptor.
class RevealAccess:
    """
    A data descriptor that sets and returns values normally
    and prints a message logging their access.
    """

    def __init__(self, value=None, name='var'):
        self.value = value
        self.name = name

    def __get__(self, instance, owner):
        print('__get()__ is Retrieving', self.name)
        return self.value

    def __set__(self, instance, value):
        print('__set__ is Updating', self.name)
        self.value = value

    def __delete__(self, instance):
        print('__delete__ is Deleting', self.name)
        del self.name


class Foo:
    x = RevealAccess(10, 'var "x"')
    y = 5


def main():
    # get
    f = Foo()
    print(f.x)

    # set
    f.x = 20
    print(f.x)
    print(f.y)

    # delete
    del f.x
    try:
        print(f.x)
    except AttributeError as e:
        print(e)


if __name__ == '__main__':
    main()
