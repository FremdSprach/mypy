"""
Return a list in reverse order, either with
subscription tricks or built-in method reverse().

[Note]
array.reverse() will change array itself,
while reversed(array) will just give a result of revered array,
leaving original array untouched.
"""
from random import randint


def reverse_list(array):
    # Use a subscription trick(slicing operator).
    # Syntax: reversed_list = list[start:stop:step]
    return array[::-1]


def main():
    # A list of consecutive sequence.
    test_array = [t for t in range(10)]
    print('Before reverse:', test_array)
    print('After  reverse:', reverse_list(test_array))
    test_array.reverse()
    print('After  reverse:', test_array)
    print('After  reverse:', [t for t in reversed(test_array)])

    # A list in chaos order.
    test_array = []
    for i in range(10):
        test_array.append(randint(0, 9))
    print('Before reverse:', test_array)
    print('After  reverse:', reverse_list(test_array))
    test_array.reverse()
    print('After  reverse:', test_array)
    print('After  reverse:', [t for t in reversed(test_array)])


if __name__ == '__main__':
    main()
