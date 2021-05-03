"""
The built-in zip function "zips" two lists.
Write your own implementation of this function.
Define a function named zap. The function takes two parameters, a and b.
 These are lists.
Your function should return a list of tuples. Each tuple should contain
one item from the a list and one from b.
You may assume a and b have equal lengths.
If you don't get it, think of a zipper.
"""


def zap(lista1, lista2):
    output = []
    for x in range(len(lista1)):
        a, b = lista1[x], lista2[x]
        output.append((a, b))
    return output


if __name__ == "__main__":
    print(zap([1, 2, 3], [4, 5, 6]))
