"""
https://leetcode.com/problems/search-a-2d-matrix/

74. Search a 2D Matrix
"""

def searchMatrix(matrix: list, target: int) -> bool:
    def inner_search(array: list):

        l, r = 0, len(array) - 1

        while l < r:
            m = l + ((r - l) // 2)
            if array[m] > target:
                r = m - 1
            elif array[m] < target:
                l = m + 1
            else:
                return True

        return target in (array[l], array[r])

    left_arr, right_arr = 0, len(matrix) - 1

    while left_arr < right_arr:
        m_arr = left_arr + ((right_arr - left_arr) // 2)
        if matrix[m_arr][-1] < target:
            left_arr = m_arr + 1
        elif matrix[m_arr][0] > target:
            right_arr = m_arr - 1
        else:
            return inner_search(matrix[m_arr])

    return inner_search(matrix[left_arr]) or inner_search(matrix[right_arr])