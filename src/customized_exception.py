"""
Define your own Exception rather than use built-in Exceptions.
"""
import logging
from traceback import format_exc

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def division(x, y): return x // y


class DivisorZeroException(Exception):
    pass


def main():
    # Built-in Exception.
    try:
        quotient = 5 / 0
    except ZeroDivisionError as e:
        logging.error(e, exc_info=True)

    # An alternative.
    try:
        quotient = 5 / 0
    except ZeroDivisionError as e:
        logging.error(format_exc())

    # Customized Exception.
    try:
        raise DivisorZeroException
    except DivisorZeroException as e:
        logging.error(e, exc_info=True)

    # An alternative.
    try:
        raise DivisorZeroException
    except DivisorZeroException as e:
        logging.error(format_exc())


if __name__ == '__main__':
    main()
