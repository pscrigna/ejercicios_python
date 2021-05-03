"""
Define a function named triple_and that takes three parameters and returns
True only if they are all True and False otherwise.
"""


def triple_and(a, b, c):
    return a and b and c


if __name__ == "__main__":
    print(triple_and(True, False, True))
    print(triple_and(True, True, True))
