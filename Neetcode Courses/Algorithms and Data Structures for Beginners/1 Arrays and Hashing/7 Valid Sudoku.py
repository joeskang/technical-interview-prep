"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/


"""

def isValidSudoku(board: list) -> bool:

    def inner_validate(indices: list) -> bool:
        inner_set = set()
        for index in indices:
            matrix_row = index // 9
            matrix_column = index % 9
            if piece := board[matrix_row][matrix_column] in inner_set:
                return False
            if piece != '.':
                inner_set.add(piece)
        return True

    def check_row(row_index):
        row_start = row_index * 9
        indices = list(range(row_start, row_start + 9))
        return inner_validate(indices)

    def check_column(column_index):
        indices = list(range(column_index, 72 + column_index, 9))
        return inner_validate(indices)

    def check_square(top_left_index):
        indices = []
        for i in range(3):
            row_start = i * 9 + top_left_index
            indices += list(range(row_start, row_start + 3))
        return inner_validate(indices)


    for i in range(9):
        row_index, column_index, top_left_index = i * 9, i, ((i % 3) * 3) + (27 * (i // 3))
        if not check_row(row_index) or not check_column(column_index) or not check_square(top_left_index):
            return False

    return True

def test1():
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    assert isValidSudoku(board)

if __name__ == "__main__":
    test1()
