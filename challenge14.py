"""
A string is a palindrome when it is the same when read backwards.
For example, the string "bob" is a palindrome. So is "abba".
But the string "abcd" is not a palindrome, because "abcd" != "dcba".
Write a function named palindrome that takes a single string as its parameter.
Your function should return True if the string is a palindrome,
and False otherwise.
"""


def palindrome(frase1, frase2):

    for x in range(1, len(frase1)):
        # print(f' frase1: {frase1[x-1]}, frase2: {frase2[-x]}')
        if frase1[x-1] != frase2[-x]:
            return False
    return True


if __name__ == "__main__":
    print(palindrome("QWERTY", "YTREWQ"))
    print(palindrome("ABCD", "ABCD"))
