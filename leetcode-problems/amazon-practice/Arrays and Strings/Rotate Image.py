"""
This is a challenging problem, make sure to understand

started 6/25/2022
finished 6/26/2022
"""

class List(list):
    pass

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def layer_rotator(length, m, n):
            """
                start_pos = [x, y]
                will assume it's the top left one
            """
            for i in range(length - 1 - m):
                new_n = n + i
                new_m = m + i
                # the_four = [[m, new_n], [new_m, n + length - 1], [m + length - 1, n + length - 1 - i], [m + length - 1 - i, n], [m, new_n]]
                the_four = [[m, new_n], [new_m, length - 1], [length - 1, length - 1 - i], [length - 1 - i, n], [m, new_n]]
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


if __name__ == "__main__":
    in_ = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol = Solution()
    sol.rotate(in_)