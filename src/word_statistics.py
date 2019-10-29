"""
Use Counter container in the module called 'collections'
to give a statistic view of every word in a sentence.
"""
from collections import Counter


def main():
    s = "the;this;that;the;ok;this;that;hello"
    c = Counter(s.split(';'))
    print(dict(c.items()))

    for k, v in c.items():
        print('%-10s %2d' % (k, v))


if __name__ == '__main__':
    main()
