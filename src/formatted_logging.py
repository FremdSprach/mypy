"""
Logging with datetime format.
"""
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def main():
    # different levels of logging.
    print('logging.DEBUG', logging.DEBUG)
    print('logging.INFO', logging.INFO)
    print('logging.WARNING', logging.WARNING)
    print('logging.ERROR', logging.ERROR)
    print('logging.CRITICAL', logging.CRITICAL)
    print('logging.FATAL', logging.FATAL)

    # logging at different level.
    logging.debug('logging DEBUG log.')
    logging.info('logging INFO log.')
    logging.warning('logging WARNING log.')
    logging.error('logging ERROR log.')
    logging.critical('logging CRITICAL log.')
    logging.fatal('logging FATAL log.')  # the same with critical.


if __name__ == '__main__':
    main()
