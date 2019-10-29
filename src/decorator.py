"""
A simple decorator.
"""
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO)


# A decorator is a function that can
# do some preceding and postdate works to another function.
# The decorator method below is a simple decorator.
def decorator(func):
    def wrapper(*args, **kwargs):
        """
        A short docstring for the wrapper.
        :param args:
        :return: None.
        """
        print('Preceding function stuff.')
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        func(*args, **kwargs)
        print('Postdate function stuff.')

    return wrapper


# A dummy usage.
def foo(*args, **kwargs):
    print('A function that needs some decoration.')


foo = decorator(foo)


# A more compact usage.
@decorator
def bar(*args, **kwargs):
    print('A function that needs some decoration.')


# Some subtle details that needs more attention.
@decorator
def decorated(*args, **kwargs):
    """
    This method needs some decorations from a decorator.
    The method's name and docstring would be over-ridden
    by the name and docstring of the wrapper method in the decorator.

    :return: None.
    """
    print('A function that needs some decoration.')


# In order to avoid method name and docstring over-ridden,
# use a method in the functools called 'wraps' to define a
# new decorator that is name and docstring safe.
def decorator_safe(func):
    # wraps is a decorator too, it would make a copy of
    # __name__, __doc__ and so on from the original method.
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        A short docstring for the wrapper.
        :param args:
        :return: None.
        """
        print('Preceding function stuff.')
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        func(*args, **kwargs)
        print('Postdate function stuff.')

    return wrapper


@decorator_safe
def decorated_safe(*args, **kwargs):
    """
    This method needs some decorations from a decorator.
    The method's name and docstring would 'NOT' be over-ridden
    by the name and docstring of the wrapper method in the decorator.

    :return: None.
    """
    print('A function that needs some decoration.')


def main():
    # the common usage of decorators, like doing some logging.
    foo('1', '2')
    bar('2', '1')

    # decorated's name and docstring would be over-ridden
    # by the name decorator's inner method.
    decorated('0')
    print(decorated.__name__)
    print(decorated.__doc__)

    # decorated_safe name and docstring would 'NOT' be over-ridden
    # by the name decorator's inner method.
    decorated_safe('0')
    print(decorated_safe.__name__)
    print(decorated_safe.__doc__)


if __name__ == '__main__':
    main()
