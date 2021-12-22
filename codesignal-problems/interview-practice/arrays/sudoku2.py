def solution(grid):

    # it's a 9x9 grid
    # will use rows first
    for row in grid:
        for item in row:
            if item != '.' and row.count(item) > 1:
                return False

    # loop through columns
    for i in range(len(grid[0])):
        column = []
        for row in grid:
            char = row[i]
            if char != '.':
                if char in column:
                    return False
                column.append(char)

    # loop through 3x3's

    for i in range(9):
        row_offset = i // 3
        col_offset = i % 3
        three_mat = []
        for m in range(3):
            for n in range(3):
                char = grid[row_offset*3 + m][col_offset*3 + n]
                if char != '.':
                    if char in three_mat:
                        return False
                    three_mat.append(char)

    return True


if __name__ == "__main__":
    grid = [
        ['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']
    ]

    assert solution(grid)