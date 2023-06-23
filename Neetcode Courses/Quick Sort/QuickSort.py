
def quick_sort(array: list, s: int, e: int):
    if e - s <= 0:
        return

    pivot = array[e]
    left = s


    for i in range(s, e):
        if array[i] < pivot:
            temp = array[left]
            array[left] = array[i]
            array[i] = temp

            left += 1

    array[e] = array[left]
    array[left] = pivot

    quick_sort(array, s, left - 1)

    quick_sort(array, left + 1, e)

    return array
