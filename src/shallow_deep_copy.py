"""
Shallow and deep copy in Python.
"""
from copy import copy, deepcopy


def main():
    # Copy immutable objects.
    str0 = 'abc'
    str1 = str0
    str2 = copy(str1)
    str3 = deepcopy(str1)
    print('str0 = %s, id = %0X' % (str0, id(str0)),
          'str1 = %s, id = %0X' % (str1, id(str1)),
          'str2 = %s, id = %0X' % (str2, id(str2)),
          'str3 = %s, id = %0X' % (str3, id(str3)))

    str2 = 'foo'
    print('str0 = %s, id = %0X' % (str0, id(str0)),
          'str1 = %s, id = %0X' % (str1, id(str1)),
          'str2 = %s, id = %0X' % (str2, id(str2)),
          'str3 = %s, id = %0X' % (str3, id(str3)))

    str3 = 'bar'
    print('str0 = %s, id = %0X' % (str0, id(str0)),
          'str1 = %s, id = %0X' % (str1, id(str1)),
          'str2 = %s, id = %0X' % (str2, id(str2)),
          'str3 = %s, id = %0X' % (str3, id(str3)))

    # Copy simple mutable objects.
    array0 = list('abc')
    array1 = array0
    array2 = copy(array1)
    array3 = deepcopy(array1)
    print('array0 = %s, id = %0X' % (array0, id(array0)),
          'array1 = %s, id = %0X' % (array1, id(array1)),
          'array2 = %s, id = %0X' % (array2, id(array2)),
          'array3 = %s, id = %0X' % (array3, id(array3)))

    array1[-1] = 'd'
    print('array0 = %s, id = %0X' % (array0, id(array0)),
          'array1 = %s, id = %0X' % (array1, id(array1)),
          'array2 = %s, id = %0X' % (array2, id(array2)),
          'array3 = %s, id = %0X' % (array3, id(array3)))

    array2[-1] = 'e'
    print('array0 = %s, id = %0X' % (array0, id(array0)),
          'array1 = %s, id = %0X' % (array1, id(array1)),
          'array2 = %s, id = %0X' % (array2, id(array2)),
          'array3 = %s, id = %0X' % (array3, id(array3)))

    array3[-1] = 'f'
    print('array0 = %s, id = %0X' % (array0, id(array0)),
          'array1 = %s, id = %0X' % (array1, id(array1)),
          'array2 = %s, id = %0X' % (array2, id(array2)),
          'array3 = %s, id = %0X' % (array3, id(array3)))

    # Copy complex mutable objects, such as dict, list of lists.
    dict0 = {0: 'a', 1: 'b', 2: 'c'}
    dict1 = dict0
    dict2 = copy(dict1)
    dict3 = deepcopy(dict1)
    print('dict0 = %s, id = %0X' % (dict0, id(dict0)),
          'dict1 = %s, id = %0X' % (dict1, id(dict1)),
          'dict2 = %s, id = %0X' % (dict2, id(dict2)),
          'dict3 = %s, id = %0X' % (dict3, id(dict3)))

    dict1.update({3: 'd'})
    print('dict0 = %s, id = %0X' % (dict0, id(dict0)),
          'dict1 = %s, id = %0X' % (dict1, id(dict1)),
          'dict2 = %s, id = %0X' % (dict2, id(dict2)),
          'dict3 = %s, id = %0X' % (dict3, id(dict3)))

    dict2.update({4: 'e'})
    print('dict0 = %s, id = %0X' % (dict0, id(dict0)),
          'dict1 = %s, id = %0X' % (dict1, id(dict1)),
          'dict2 = %s, id = %0X' % (dict2, id(dict2)),
          'dict3 = %s, id = %0X' % (dict3, id(dict3)))

    dict3.update({5: 'f'})
    print('dict0 = %s, id = %0X' % (dict0, id(dict0)),
          'dict1 = %s, id = %0X' % (dict1, id(dict1)),
          'dict2 = %s, id = %0X' % (dict2, id(dict2)),
          'dict3 = %s, id = %0X' % (dict3, id(dict3)))


if __name__ == '__main__':
    main()
