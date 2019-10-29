"""
Find the k-th greatest number in an unsorted list,
using the quick-sort algorithm for reference.
"""


# The classic partition implementation of quick-sort algorithm.
def partition(array, low, high):
    i = low

    for j in range(low, high):
        if array[j] <= array[high]:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]

    return i


def qsort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        qsort(array, low, p - 1)
        qsort(array, p + 1, high)


def find_kth(array, low, high, k):
    if low < high:
        p = partition(array, low, high)
        if p == k:
            return array[p]
        if p < k:
            return find_kth(array, p + 1, high, k)
        if p > k:
            return find_kth(array, low, p - 1, k)
    if low == high:
        return array[low]


def main():
    test_array = [1, 3, 2, 4]
    array_size = len(test_array)

    # Apply quick-sort.
    qsort(test_array, 0, array_size - 1)
    print(test_array)

    # Find the k-th greatest.
    for i in range(len(test_array)):
        print('%d-th greatest number is' % i, find_kth(test_array, 0, len(test_array) - 1, i))


if __name__ == '__main__':
    main()
