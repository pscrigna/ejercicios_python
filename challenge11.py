"""
Define a function named largest_difference that takes a list
of numbers as its only parameter.

Your function should compute and return the difference between
the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3])
should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""


def largest_difference(lista):
    minimo = 100
    maximo = -100

    for x in lista:
        if x < minimo:
            minimo = x
        elif x > maximo:
            maximo = x
    return maximo - minimo


if __name__ == "__main__":
    print(largest_difference([1, 1, 1, 1, 1, 1]))
    print(largest_difference([1, 1, 2, 1, 1, 10]))
