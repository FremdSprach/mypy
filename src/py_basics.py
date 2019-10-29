"""
This file is a collection of basic usage of Python.
"""
import logging
from traceback import format_exc

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def main():
    # Swap 2 numbers.
    a, b = 1, 2
    print('a = %d' % a, 'b = %d' % b)

    a, b = b, a
    print('a = %d' % a, 'b = %d' % b)

    # Built-in join method.
    x = 'abc'
    y = 'def'
    z = ['d', 'e', 'f']
    print('x = %s' % x, 'y = %s' % y, 'z = %s' % z)
    print('x.join(y) = %s' % x.join(y), 'x.join(z) = %s' % x.join(z))
    if x.join(y) == x.join(z):
        print('x.join(y) = x.join(z)')

    # Strings in Python are not immutable.
    str1 = 'abc'
    str2 = 'abc'
    print('%8s' % str1, '%0X' % id(str1), '%8s' % str2, '%0X' % id(str2))
    str1 += 'def'
    print('%8s' % str1, '%0X' % id(str1), '%8s' % str2, '%0X' % id(str2))

    # Built-in zip method.
    print(zip(x, y), type(zip(x, y)))
    print(list(zip(x, y)))
    print(tuple(zip(x, y)))
    print(dict(zip(x, y)))

    # Built-in bytes method.
    print(bytes(x, 'utf-8'))
    print(bytes(x, 'utf-8').decode('utf-8'))

    # Concatenate 2 lists.
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(x, '+', y, '=', x + y)

    # Print a list in sorted order without using sort.
    print(x + y, '->', list(set(x + y)))

    # Given two lists, get intersection, union and difference.
    array1 = [1, 2, 3, 4]
    array2 = [3, 4, 5, 6]

    # intersection.
    intersection = [a for a in array1 if a in array2]
    print('intersection of %s and %s is %s' % (array1, array2, intersection))

    # union.
    union = list(set(array1 + array2))
    print('union of %s and %s is %s' % (array1, array2, union))

    # difference.
    difference = [a for a in array1 if a not in intersection] + \
                 [a for a in array2 if a not in intersection]
    print('difference of %s and %s is %s' % (array1, array2, difference))

    # Round a float.
    print('%.3f' % 1.3335)
    print('%.03f' % 1.3335)

    # Delete an entry in a dict.
    test_dict = {'name': 'Jack', 'age': 10, 'gender': 'male'}
    print(test_dict)
    del test_dict['gender']
    print(test_dict)
    test_dict.pop('age')
    print(test_dict)

    # any() and all() methods. Similar to OR, AND operators.
    # any() returns False if iterable is empty or all elements are False.
    # and it returns True once a True element is encountered.
    # all() returns True if iterable is empty or all elements are True.
    # and it returns False once a False is encountered.
    print(any([False, False, False, False]))
    print(any([False, True, False, False]))
    print(any([True, False, False, False]))
    print(all([True, True, True, True]))
    print(all([False, True, True, False]))
    print(all([False, False, False]))

    # strip(), lstrip(), rstrip().
    line = ' abc def  '
    print('Before strip(): |' + line + '|')
    print('After  strip(): |' + line.strip() + '|')
    print('After lstrip(): |' + line.lstrip() + '|')
    print('After rstrip(): |' + line.rstrip() + '|')

    # character occurrences in a string.
    line = 'start-the-that-this-self-end.'
    chars = sorted(list(set(line)), key=line.index)
    for c in chars:
        print('%c occurred %d time(s) in %s' % (c, line.count(c), line))

    # cast between different types.
    try:
        print('int("1.4")', int("1.4"))
    except ValueError as e:
        print(format_exc())
    print('int(1.4)', int(1.4))

    # Common Exceptions.
    try:
        open('demo.txt', 'r')  # open a non-existing file.
    except FileNotFoundError as e:
        logging.error(format_exc())

    try:
        print(foobar)
    except NameError as e:
        logging.error(format_exc())


if __name__ == '__main__':
    main()
