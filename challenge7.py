"""
Write a function named add_dots that takes a string and adds "."
in between each letter.
For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots
that removes all dots from a string. For example, calling remove_dots
("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string))
should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""


def add_dots(frase):
    out = ""
    for x in frase:
        out += x + "."
    return out


def remove_dots(frase):
    out = ""
    for x in frase:
        if x != ".":
            out += x
    return out


if __name__ == "__main__":
    print(add_dots("Hola"))
    print(remove_dots("H.o.l.a."))
    print("f.r.a.s.e.".replace(".", ""))