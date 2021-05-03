"""
The goal of this challenge is to analyze a string to check if it
contains two of the same letter in a row. For example, the string
"hello" has l twice in a row, while the string "nono" does not have
two identical letters in a row.

Define a function named double_letters that takes a single parameter.
The parameter is a string. Your function must return True if there are
two identical letters in a row in the string, and False otherwise.
"""

import pytest


def double_letters(frase):
    """ Verifica si hay dos letras iguales seguidas en una frase.
        Toma un string como parametro y retorna True or False.
    """
    for x in range(len(frase)-1):
        if frase[x] == frase[x+1]:
            return True
    return False


def test_double_letters_ok():
    frase = "Hello"
    assert double_letters(frase) is True


def test_double_letters_nok():
    frase = "ABCDEFGH"
    assert double_letters(frase) is False


@pytest.mark.parametrize("frase, salida", [("LLUEVE", True), ("HOY", False)])
def test_double_letters_paremetrize(frase, salida):
    assert double_letters(frase) == salida


if __name__ == "__main__":
    print(f'Comentario: {double_letters.__doc__}')
    print(double_letters("Hello"))
    print(double_letters("asdf"))
