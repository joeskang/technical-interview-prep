

"""
sort list with even numbers in the beginning


"""
def even_odd(array: list) -> None:
    left, right = 0, len(array) - 1

    while left < right:

        # check left is even
        if array[left] % 2:
            left += 1

        # left is odd and right is even
        elif not array[right] % 2:
            array[left], array[right] = array[right], array[left]
            left += 1

        # left is odd and right is odd
        else:
            right -= 1


def test_1():
    my_array = [1,2,3,4,6,8]
    even_odd(my_array)
    print(my_array)

    for i in range(3):
        assert not my_array[i] % 2, f"found following odd number {my_array[i]}"

if __name__ == '__main__':
    test_1()
