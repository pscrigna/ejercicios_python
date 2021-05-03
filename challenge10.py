"""
Write a function that takes a list of lists and flattens
it into a one-dimensional list.

Name your function flatten.
It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])

Should return the list:

[1, 2, 3, 4]
"""


def flatten(lista1, lista2):
    output = []

    for x in lista1:
        output.append(x)
    for y in lista2:
        output.append(y)

    return output


if __name__ == "__main__":
    print(flatten([1, 2, 3, 4], [9, 10, 11, 12]))
