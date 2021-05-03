"""
Write a function named capital_indexes.
The function takes a single parameter,which is a string.
Your function should return a list of all the indexes in
the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return
the list [0, 2, 4].
"""
import pytest


def capital_indexes(frase):
    """Retorna los indices de la lista donde hay letras en mayusculas"""
    posiciones = []
    for x in range(len(frase)):
        ascii = ord(frase[x])
        condition = ascii > 64 and ascii < 91
        if condition:
            posiciones.append(x)
    return posiciones


def test_capital_indexes():
    frase = "HoLa"
    assert_list = [0, 2]
    assert capital_indexes(frase) == assert_list


@pytest.mark.parametrize("frase, lista_out", [("HoLa", [0, 2]), ("HOY", [0, 1, 2])])
def test_capital_indexes_paremetrize(frase, lista_out):
    assert capital_indexes(frase) == lista_out


if __name__ == "__main__":
    print(capital_indexes.__doc__)
    frase = "HolA Mundo!"
    print(capital_indexes(frase))
