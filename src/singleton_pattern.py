"""
The singleton pattern implemented in Python.

In software engineering, the singleton pattern is a design pattern
that restricts the instantiation of a class to one object.
This is useful when exactly one object is needed to coordinate actions across the system.
The concept is sometimes generalized to systems that operate more efficiently
when only one object exists, or that restrict the instantiation to a certain number of objects.

Python modules are naturally Singleton Patterns, because importing a module
would make Python generate a .pyc file, next time the same module is imported,
the .pyc file instead of the module itself would be loaded. That is:

# First define a class in one file called singleton.py
# under the package 'singletons'.
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
# Then use the singleton instance by Python import.
from singletons.singleton import singleton
"""
from threading import Thread, Lock
from time import sleep


# The second way other than using the Python module is using decorators.
def singleton(cls):
    # Use a dictionary to store the only instance of a class.
    _instance = {}

    def _singleton(*args, **kwargs):
        # make sure _instance only gets one instance.
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    # now _instance can only contain one instance of the given class.
    return _singleton


@singleton
class Foo:
    def __init__(self, bar=None):
        self.bar = bar
        print('__init__() method of a singleton pattern class Foo.')


# The third way, implement singleton in a class.
class Bar:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # use reflection here to make sure
        # there is one and only one instance of the class itself.
        if not hasattr(Bar, '_instance'):
            Bar._instance = Bar(*args, **kwargs)
        return Bar._instance


# The fourth way, implement singleton in a class, support safe multi threads.
class Singleton:
    _instance_lock = Lock()

    def __init__(self, *args, **kwargs):
        sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            # A lock is needed here to make sure
            # only one instance is being created at the same time.
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


# Most recommended way to implement singletons is using __new__ method.
class SingletonFinal:
    _instance_lock = Lock()

    def __init__(self, *args, **kwargs):
        sleep(1)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SingletonFinal._instance_lock:
                if not hasattr(cls, '_instance'):
                    SingletonFinal._instance = super().__new__(cls)
        return SingletonFinal._instance


def task1():
    obj = Singleton.get_instance()
    print(obj)


def task2():
    obj = SingletonFinal()
    print(obj)


def main():
    # Singleton realized with decorator.
    f1 = Foo()
    f2 = Foo()
    print('The 2 instances of class Foo would use the same address.')
    print('Address of instance f1: %0X, name of f1: %s' % (id(f1), f1.__class__.__name__))
    print('Address of instance f2: %0X, name of f2: %s' % (id(f2), f2.__class__.__name__))

    # Singleton realized with class.
    # Incorrect usage.
    single = Bar()
    # Correct usage.
    b1 = Bar.get_instance()
    b2 = Bar.get_instance()
    print('Address of instance b1: %0X, name of b1: %s' % (id(b1), b1.__class__.__name__))
    print('Address of instance b2: %0X, name of b2: %s' % (id(b2), b2.__class__.__name__))

    # Singleton in multi threads situation.
    for i in range(10):
        t = Thread(target=task1)
        t.start()

    # Best singleton practice, multi threads situation.
    for i in range(10):
        t = Thread(target=task2)
        t.start()


if __name__ == '__main__':
    main()
