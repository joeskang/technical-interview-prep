"""
This is a challenging problem, make sure to understand

started 6/25/2022
"""

# TODO: complete

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def layer_rotator(length, x, y):
            """
                start_pos = [x, y]
                will assume it's the top left one
            """
            for i in range(length - 1):
                new_y = y + i
                new_x = x + i
                the_four = [[x, new_y], [new_x, y + length - 1], [x + length - 1, y + length - 1 - i], [x + length - 1 - i, y]]
                temp = past = None
                for coordinates in the_four:
                    if past is None:
                        past = matrix[coordinates[0]][coordinates[1]]
                    else:
                        temp = matrix[coordinates[0]][coordinates[1]]
                        matrix[coordinates[0]][coordinates[1]] = past
                        past = temp
        for j in range(len(matrix)):
            x = y = j
            length = len(matrix) - j
            layer_rotator(length, x, y)