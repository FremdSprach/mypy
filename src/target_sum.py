"""
Given a sum, find all occurrences of
the index of a pair of numbers from a list that
add up to the sum.
"""


# For this time complexity is O(n^2).
def target_sum(array, summation):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == summation:
                yield [i, '(' + str(array[i]) + ')', j, '(' + str(array[j]) + ')']


def main():
    test_array = [x for x in range(100)]
    for t in target_sum(test_array, 40):
        print(t)

    test_array = [-1, 1, -2, 2, 3, 4, 5, 6]
    for t in target_sum(test_array, 5):
        print(t)


if __name__ == '__main__':
    main()
