"""
Define a function named list_xor.
Your function should take three parameters: n, list1 and list2.
Your function must return whether n is exclusively in list1 or list2.
In other words, if n is in both lists or in none of the lists, return False.
If n is in only one of the lists, return True.
"""


def list_xor(n, lista1, lista2):
    lst1 = False
    lst2 = False

    if n in lista1:
        lst1 = True
    if n in lista2:
        lst2 = True
    return not (lst1 == lst2)


if __name__ == "__main__":
    print(list_xor(2, [1, 2, 3], [3, 7, 8]))
