def solution(matrix):
    # old row = new column reversed
    # old column = new row

    iterations = len(matrix[0]) - 1
    row = 0

    while iterations > 0 and row < len(matrix):
        # row will serve as the offset
        for i in range(iterations):
            past = 0
            old_col = -1
            old_row = -1
            for _ in range(4):
                if old_col < 0 or old_row < 0:
                    old_col = i + row
                    old_row = row

                new_col = len(matrix) - 1 - old_row
                new_row = old_col
                if not past:
                    past = matrix[old_row][old_col]
                past, matrix[new_row][new_col] = matrix[new_row][new_col], past
                old_row, old_col = new_row, new_col

        iterations -= 2
        row += 1

    return matrix
