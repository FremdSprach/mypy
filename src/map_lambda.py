"""
Use map and lambda expression together to
make the codes clean and beautiful.
"""


def square(x): return x * x


def multiply(x, y): return list(map(lambda s, t: s * t, x, y))


def main():
    # Ordinary style.
    squares = list(map(square, range(10)))
    print(squares)

    # A more compact way.
    squares = list(map(lambda x: x * x, range(10)))
    print(squares)

    # Another alternative way.
    xes = [x for x in range(10)]
    print(multiply(xes, xes))

    # Filter numbers that are greater than 10 in the list 'squares'.
    result = [x for x in squares if x >= 10]
    print(result)

    # Filter odd numbers.
    odds = list(filter(lambda x: x % 2 == 1, range(10)))
    print(odds)

    # List induction alternative.
    odds = [x for x in range(10) if x % 2 == 1]
    print(odds)

    # Sort an array of dicts with lambda expression.
    test_array = [
        {'name': 'Anna', 'age': 10},
        {'name': 'Catherine', 'age': 8}
    ]
    print(sorted(test_array, key=lambda dict_item: dict_item['name']))
    print(sorted(test_array, key=lambda dict_item: dict_item['age']))
    test_array.sort(key=lambda dict_item: dict_item['name'])
    print(test_array)
    test_array.sort(key=lambda dict_item: dict_item['age'])
    print(test_array)

    # Sort a list with lambda expression, small to big.
    test_array = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    test_array = [[i, test_array[i]] for i in range(len(test_array))]
    test_array.sort(key=lambda array_item: array_item[1])
    print([test_array[i][1] for i in range(len(test_array))])

    # Sort a list with lambda expression, with positives
    # from small to big, and negatives from big to small.
    test_array = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    positives = [t for t in test_array if t >= 0]
    negatives = [t for t in test_array if t < 0]
    positives = [[i, positives[i]] for i in range(len(positives))]
    negatives = [[i, negatives[i]] for i in range(len(negatives))]
    positives.sort(key=lambda array_item: array_item[1])
    negatives.sort(key=lambda array_item: array_item[1])
    positives = [positives[i][1] for i in range(len(positives))]
    negatives = [negatives[i][1] for i in range(len(negatives))]
    test_array = positives + negatives
    print(test_array)

    # Sort a list of tuples with lambda expression.
    test_array = [(0, 'c'), (1, 'b'), (2, 'a')]
    print(sorted(test_array, key=lambda array_item: array_item[0]))
    print(sorted(test_array, key=lambda array_item: array_item[1]))
    test_array.sort(key=lambda array_item: array_item[0])
    print(test_array)
    test_array.sort(key=lambda array_item: array_item[1])
    print(test_array)

    # Sort a list of strings by their lengths in reverse order.
    test_array = [
        'a', 'ab', 'cd', 'c',
        'that', 'ssf', 'sds',
        'Challenge', 'great'
    ]
    test_array = [[len(t), t] for t in test_array]
    test_array.sort(key=lambda array_item: array_item[0], reverse=True)
    test_array = [test_array[i][1] for i in range(len(test_array))]
    print(test_array)


if __name__ == '__main__':
    main()
