"""
The difference between items() and iteritems().

In Python 2.x, items() will retrieve all key:value pairs from a dict,
and returns a copy of the pairs, while iteritems() returns an iterator instead.

In Python 3.x, items() is kept and is consistent with
items() in Python 2.x, iteritems() method is depreciated.
"""
from collections import OrderedDict

import json
import operator


def main():
    # The test dict.
    users = {
        'Sarah': {
            'sex': 'female',
            'age': 10
        },
        'Alice': {
            'sex': 'female',
            'age': 16
        },
    }

    print(users)
    print(users.items())
    print(type(users.items()))
    for k, v in users.items():
        print(k, v['sex'], v['age'])

    # Sort dict by keys.
    print(users)

    sorted_users = sorted(users.items(), key=lambda kv: kv[0])
    sorted_users = {u[0]: u[1] for u in sorted_users}

    print(sorted_users)

    # An alternative to the above.
    print(users)
    sorted_users = sorted(users.items(), key=operator.itemgetter(0))
    sorted_users = {u[0]: u[1] for u in sorted_users}
    print(sorted_users)

    # dict and json.
    d = {0: 'a', 1: 'b', 2: 'c'}

    # dumps means dump a string into json.
    j = json.dumps(d)
    print(d)
    print(j)

    # loads means load a string into dict.
    d = json.loads(j)
    print(d)
    print(j)


if __name__ == '__main__':
    main()
