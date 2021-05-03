"""
Define a function named all_equal that takes a list and checks
whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""


def all_equal(lista):
    for x in range(len(lista)-1):
        if lista[x] != lista[x + 1]:
            return False
    return True


if __name__ == "__main__":
    print(all_equal([1, 1, 1]))
    print(all_equal([2, 3, 5]))
