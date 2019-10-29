"""
Assertions in Python.
"""
import traceback
from traceback import format_exc


def main():
    # A case where assertion passed.
    try:
        assert 1 + 1 == 2
    except AssertionError as e:
        print(format_exc())
    else:
        print('Calculation looks right.')

    # Implicit assertion, with no assertion error message.
    try:
        assert 1 + 1 == 1
    except AssertionError as e:
        print(format_exc())

    # Explicit assertion specifying error message.
    try:
        assert 1 + 1 == 1, 'Wrong calculation!'
    except AssertionError as e:
        print(format_exc())


if __name__ == '__main__':
    main()
