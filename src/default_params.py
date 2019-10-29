"""
Because default parameters remain in memory after calls
to a method, so unexpected results would come up
if default parameters are not properly dealt with.
"""


# Bad practice.
def foo(n, ret=[]):
    for i in range(n):
        ret.append(i)
    return ret


# Good practice.
def bar(n, ret=None):
    if ret is None:
        ret = []
    for i in range(n):
        ret.append(i)
    return ret


def main():
    # expected result:
    # 2 -> 0, 1
    # 3 -> 0, 1, 2

    print(foo(2))
    print(foo(3))  # result is 0, 1, 0, 1, 2

    print(bar(2))
    print(bar(3))  # result is 0, 1, 2


if __name__ == '__main__':
    main()
