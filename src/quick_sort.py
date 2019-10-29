"""
Quick-Sort algorithm implemented in Python.
Time complexity is O(n*log(n)).
"""


def quick_sort(array):
    if len(array) < 2:  # the condition to break recursion.
        return array
    pivot = array[-1]  # pick the last element as the pivot.

    array_left = [a for a in array[:-1] if a <= pivot]
    array_right = [a for a in array[:-1] if a > pivot]

    return quick_sort(array_left) + [pivot] + quick_sort(array_right)


def main():
    test_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(quick_sort(test_array))


if __name__ == '__main__':
    main()
