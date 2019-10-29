"""
A Generator is a special case of advanced Python iterator.
"""


# A simple generator.
def use_generator(n):
    for i in range(n):
        yield i


# A more practical one.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    # we just get a list of sequence here.
    for s in use_generator(5):
        print(s, end=',')
    print()

    # now we want get the leading 4 fibonacci numbers.
    fb = fibonacci()
    print(next(fb), end=',')
    print(next(fb), end=',')
    print(next(fb), end=',')
    print(next(fb), end=',')
    print()

    # get as many fibonacci numbers as we want.
    for _ in range(20):
        print(next(fb), end=',')


if __name__ == '__main__':
    main()
