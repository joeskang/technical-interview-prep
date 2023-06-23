"""
NeetCode's implementation of mergeSort
"""


def merge_sort(array: list, start_index: int, end_index: int) -> list:
    # base case, end_index and start_index are the same
    if end_index - start_index + 1 <= 1:
        return array

    mid_index = (start_index + end_index) // 2

    # dfs, sort left half first
    merge_sort(array, start_index, mid_index)

    # sort right half next
    merge_sort(array, mid_index + 1, end_index)

    # then, merge
    merge(array, start_index, mid_index, end_index)

    return array

# merge in place
def merge(array: list, start_index: int, mid_index: int, end_index: int) -> None:

    # temp arrays
    left_half = array[start_index: mid_index+1]
    right_half = array[mid_index + 1: end_index + 1]

    i = j = 0
    k = start_index

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1


    # deal with the remaining halfs
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1


