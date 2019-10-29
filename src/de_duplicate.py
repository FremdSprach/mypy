"""
Remove duplicate entries in a given list.
"""

from random import randint


def de_duplicate(array):
    # set will sort its elements automatically.
    unique_array = set(array)
    result = list(unique_array)

    # to restore the original order, just use the built-in method sort.
    result.sort(key=array.index)
    return result


def purify_str(string):
    # set will sort its elements automatically.
    string_list = list(string)
    unique_str = set(string_list)
    result = list(unique_str)

    # to restore the original order, just use the built-in method sort.
    result.sort(key=string_list.index)
    return ''.join(result)


def count(array, e):
    result = 0
    for a in array:
        if a == e:
            result += 1
    return result


def main():
    test_array = []
    for i in range(20):
        test_array.append(randint(0, 9))
    print('Before de-duplication:', test_array)

    unique_test_array = de_duplicate(test_array)
    print('After  de-duplication:', unique_test_array)

    # Find all occurrences of unique entries.
    for e in unique_test_array:
        occurrences = count(test_array, e)
        print('%d occur %d time(s) in original array.' % (e, occurrences))

    # De-duplicate a string.
    test_string = 'abc-abc-dec'
    print(test_string)
    print(purify_str(test_string))


if __name__ == '__main__':
    main()
