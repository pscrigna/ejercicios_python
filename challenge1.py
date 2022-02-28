"""
Write a function named capital_indexes.
The function takes a single parameter,which is a string.
Your function should return a list of all the indexes in
the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return
the list [0, 2, 4].
"""

import pytest

ASCII_CAP_MIN = 65
ASCII_CAP_MAX = 90 


def capital_indexes(phrase):
    """
    Return a list of all the indexes in the string that have capital letters.
    """
    capital_indexes = []
    for index, character in enumerate(phrase):
        ascii = ord(character)
        condition = ascii >= ASCII_CAP_MIN and ascii <= ASCII_CAP_MAX
        if condition:
            capital_indexes.append(index)
    return capital_indexes


def test_capital_indexes():
    phrase = "HolAZ"
    assert_list = [0, 3, 4]
    assert capital_indexes(phrase) == assert_list


@pytest.mark.parametrize("phrase, list_out", [("HoLa", [0, 2]), ("HOY", [0, 1, 2])])
def test_capital_indexes_paremetrize(phrase, list_out):
    assert capital_indexes(phrase) == list_out


if __name__ == "__main__":
    print(capital_indexes.__doc__)
    input_string = "HolA Mundo ZZZ!"
    print(capital_indexes(input_string))
