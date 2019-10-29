"""
Generator random numbers of different types.
"""
from random import choice, randint, random, randrange, uniform


def main():
    # Get a random real number between [0.0, 1.0).
    rand = random()
    print(rand)

    # Get a random real number between [a, b].
    rand = uniform(0, 10)
    print(rand)

    # Get a random integer between [a, b].
    rand = randrange(0, 9)
    print(rand)

    # randrange is equivalent to choice(range(a, b)).
    rand = choice(range(0, 9))
    print(rand)

    # randint is alias for randrange.
    rand = randint(0, 9)
    print(rand)


if __name__ == '__main__':
    main()
