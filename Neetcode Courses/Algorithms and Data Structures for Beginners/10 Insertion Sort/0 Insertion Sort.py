"""
Insertion Sort
* stable sort
* best runtime: O(n)
* worst: O(n^2)

"""
class InsertionSorter:

    def __init__(self, array: list):
        self.array = array

    def sort(self, array: list = None) -> list:

        target = array
        if not array:
            assert self.array is not None, "No array of values was passed!"
            target = self.array

        for i in range(len(target)):

            j = i - 1
            while j >= 0 and target[j + 1] < target[j]:
                temp = target[j + 1]
                target[j + 1] = target[j]
                target[j] = temp
                j -= 1

        return target


def test1():
    import random
    my_array = list(random.randrange(0, 10) for _ in range(10))
    sorter = InsertionSorter(my_array)
    temp_array = list(my_array)
    assert sorted(temp_array) == sorter.sort()


if __name__ == "__main__":
    test1()
