"""
Old(2.x) and new(3.x) style python classes.

The main difference between these two styles is that
old style class inheritance applies depth-first order
with MRO(method resolution Order), but the new style
class applies breadth-first order with MRO.

Old style class is the default class style for Python 2.x,
programmers must inherit a class from 'object' explicitly
to use new style class.

Python 3.x removed classic style class, the default
class is new style, so there is
no need to inherit class from 'object' explicitly any more.
"""


class Grandfather:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def foo(self):
        print('This is the Grandfather class.')


class Father(Grandfather):
    # inherit initiation method from parent class.
    def __init__(self, name, age):
        Grandfather.__init__(self, name=name, age=age)

    def foo(self):
        print('This is the Father class.')


class Son(Father):
    # inherit and rewrite initiation method from parent class.
    def __init__(self, name, age, hobby):
        super(Father, self).__init__(name=name, age=age)
        self.hobby = hobby

    def foo(self):
        print('This is the Son class.')


class Daughter(Father, Grandfather):
    # use initiation method from Grandfather, not her father.
    def __init__(self, name, age):
        # super(Grandfather, self).__init__(name=name, age=age)
        super().__init__(name=name, age=age)
        # Grandfather.__init__(self, name=name, age=age)

    def foo(self):
        print('This is the Daughter class.')


class Grandson(Son):
    # discard initiation method of parent
    def __init__(self, name, age, hobby):
        super().__init__(name, age, hobby)

    def foo(self):
        print('This is the Grandson class.')


def main():
    father = Father('Father', 40)
    father.foo()

    son = Son('Son', 20, 'Maths')
    son.foo()
    print(type(son), son.__class__)
    print(son.name, son.age, son.hobby)

    if isinstance(son, Son):
        print(True)

    daughter = Daughter('Daughter', 18)
    print(daughter.name, daughter.age)

    grandson = Grandson('Grandson', 3, 'Food')
    grandson.foo()
    print(grandson.name, grandson.age, grandson.hobby)


if __name__ == '__main__':
    main()
