"""
Two strings are anagrams if you can make one from the other by rearranging
the letters.
Write a function named is_anagram that takes two strings as its parameters.
Your function should return True if the strings are anagrams,
and False otherwise.
For example, the call is_anagram("typhoon", "opython") should return True
while the call is_anagram("Alice", "Bob") should return False.
"""


def is_anagram(frase1, frase2):
    frase_1 = sorted(frase1)
    frase_2 = sorted(frase2)
    if frase_1 == frase_2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_anagram("HOLA", "ALOH"))
    print(is_anagram("HOSLA", "ALOH"))
