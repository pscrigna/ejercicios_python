"""
Define a function, random_number, that takes no parameters.
The function must generate a random integer between 1 and 100,
both inclusive, and return it.

Calling the function multiple times should (usually) return different numbers.

For example, calling random_number() some times might first return 42,
then 63, then 1.
"""

import random


def random_number():
    """ Genera un numero random entre 1 y 100 """
    return random.randint(1, 100)


def test_random_number():
    num = random_number()
    assert num < 100
    assert num > 1


if __name__ == "__main__":
    print(random_number.__doc__)
    print(f'random: {random_number()}')
    print(f'random: {random_number()}')
