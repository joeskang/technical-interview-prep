

def binary_search(array: list, target: int) -> int:
    """
    Array must be sorted!
    :param array:
    :param target:
    :return: will return the index in which the target is located
    """

    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1
        else:
            # the target was found
            return mid

    return -1

def test_binary_search():
    my_array = [1, 5, 8, 10, 112, 123, 178]
    assert binary_search(my_array, 112) == 4

if __name__ == "__main__":
    test_binary_search()

