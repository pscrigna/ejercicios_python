"""
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""


def mid(phrase):
    """
    This function takes a string as a parameter an return the middle letter
    If there is no middle letter, return tne empty string.
    """
    large = len(phrase)
    if large % 2 == 0:
        return ""
    else:
        return phrase[int(((large-1)/2))]


def test_mid_empty():
    assert mid("1234") == ""


def test_mid_value():
    assert mid("12345") == "3"


if __name__ == "__main__":
    print(mid("12345"))
    print(mid("Hola"))
    print(mid("123456789"))