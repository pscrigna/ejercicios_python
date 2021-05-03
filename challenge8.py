"""
Define a function named count that takes a single parameter.
The parameter is a string. The string will contain a single
word divided into syllables by hyphens, such as these:
"""


def count(frase):
    return frase.count("-")+1


if __name__ == "__main__":
    print(count("Ho-la"))
    print(count("sa-pi-to"))
