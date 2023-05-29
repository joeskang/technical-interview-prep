
def quick_sort(array):

    def partition(l, h):
        pivot = array[l]
        i, j = l, h
        while i < j:
            while array[i] <= pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]

        array[l], array[j] = array[j], array[l]
        return j

    def inner_function(l, h):
        if l < h:
            j = partition(l, h)
            inner_function(l, j)
            inner_function(j + 1, h)


    inner_function(0, len(array) - 1)
    return array

def test_quick_sort():
    my_array = [5, 1, 2, 9, 3, 0]
    assert sorted(my_array) == quick_sort(my_array)

if __name__ == "__main__":
    test_quick_sort()
