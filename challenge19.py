"""
Define a function named convert that takes a list of numbers as its only
parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a
single line of code.
"""


def convert(lista):
    return [str(x) for x in lista]


if __name__ == "__main__":
    lista = [1, 2, 3]
    print(f'Lista original: {lista}, lista salida: {convert(lista)}')
