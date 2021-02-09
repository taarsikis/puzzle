""" This module cheks puzzle game """


def first_property(board: list) -> bool:
    """
    The function checks the first condition, according to which the
    colored cells of each line must contain the numbers
    from 1 to 9 without repetition.
    >>> first_property([ "**** ****", "***  ****", "**   ****", "*    ****", \
" 1       ", "        *", "       **", "      ***", "     ****"])
    True
    """
    count_digits_in_row = 0
    list_of_digits_row = []
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if board[i][j].isdigit():
                count_digits_in_row+=1
                list_of_digits_row.append(int(board[i][j]))
        if len(list_of_digits_row) > len(set(list_of_digits_row)):
            return False
        count_digits_in_row = 0
        list_of_digits_row.clear()
    return True

def second_property(board: list) -> bool:
    """
    The function checks the first condition, according
    to which the colored cells of each column must contain
    the numbers from 1 to 9 without repetition.
    >>> second_property([ "**** ****", "***  ****", "**   ****", "*    ****", \
" 1       ", "        *", "       **", "      ***", "     ****"])
    True
    """
    count_digits_in_column = 0
    list_of_digits_column = []
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if board[j][i].isdigit():
                count_digits_in_column+=1
                list_of_digits_column.append(int(board[j][i]))
        if len(list_of_digits_column) > len(set(list_of_digits_column)):
            return False
        count_digits_in_column = 0
        list_of_digits_column.clear()
    return True

def third_property(board: list) -> bool:
    """
    The function checks the first condition, according
    to which each color block must contain numbers
    from 1 to 9 without repetitions.
    >>> third_property([ "**** ****", "***  ****", "**   ****", "*    ****", \
" 1       ", "        *", "       **", "      ***", "     ****"])
    True
    """
    list_of_digits_same_color = []
    count_digits_in_same_color = 0
    for j, _ in enumerate(board):
        for i in range(0, 9 - 1 - j):
            if board[i][j].isdigit():
                list_of_digits_same_color.append(int(board[i][j]))
                count_digits_in_same_color+=1
        for k in range(j + 1, 9, 1):
            if board[9 - 1 - j][k].isdigit():
                list_of_digits_same_color.append(int(board[9 - 1 - j][k]))
                count_digits_in_same_color+=1
        if len(list_of_digits_same_color) > len(set(list_of_digits_same_color)):
            return False
        list_of_digits_same_color.clear()
        count_digits_in_same_color = 0
    return True

def validate_board(board):
    """
    The function combines the verification of all three conditions.
    >>> validate_board([ "**** ****", "***  ****", "**   ****", "*    ****", \
" 1       ", "        *", "       **", "      ***", "     ****"])
    True
    """
    return first_property(board) and second_property(board) and third_property(board)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    board = [ "**** ****", "***  ****", "**   ****", "*    ****", " 1       ", "        *", "       **", "      ***", "     ****"]
    print(validate_board(board))
