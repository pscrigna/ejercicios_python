""""
The goal of this challenge is to analyze a binary string consisting of only
zeros and ones.
Your code should find the biggest number of consecutive zeros in the string.
For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter,
which is the string of zeros and ones. Your function should return
the number described above.
"""


def consecutive_zeros(lista):
    count = 0
    maximo = 0

    for x in lista:
        if x == "0":
            count += 1
        else:
            if count > maximo:
                maximo = count
            count = 0

    return maximo


if __name__ == "__main__":
    print(consecutive_zeros("1001000000110"))
    print(consecutive_zeros("10010000011110"))
    print(consecutive_zeros("0000000000110"))
