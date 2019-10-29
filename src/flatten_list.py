"""
Flatten high dimension lists into one dimension list.
"""


# Flatten a 2-D array.
def flatten_2d(array):
    return [a for sub in array for a in sub]


def main():
    test_array = [
        [1, 2, 3],
        ['a', 'b', 'c']
    ]
    print(flatten_2d(test_array))


if __name__ == '__main__':
    main()
