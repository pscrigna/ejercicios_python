"""
Imagine if your user enters "C1" and you need to see if there's an X or O in
that cell on the board. To do so, you need to translate from the string "C1"
to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2
to a tuple (row, column). Name your function get_row_col; it should take a
single parameter which is a string of length 2 consisting of an uppercase
letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because
A3 corresponds to the row at index 2 and column at index 0in the board.
"""

columnas = {
    "A": 0,
    "B": 1,
    "C": 2
}


def get_row_col(position):

    columna = columnas[position[0]]
    fila = int(position[1]) - 1
    return (fila, columna)


if __name__ == "__main__":
    print(get_row_col("A3"))
    print(get_row_col("C1"))
