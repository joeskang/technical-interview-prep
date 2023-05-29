"""
needs the following functions:
.isEmpty()
.insertWithPriority(...)
.pullHighesPriorityItem()
.peek()
"""
import math

class MaxHeap:
    """
    given that heap is a complete binary tree and binary trees can be represented by an array,
    use the functions for array representation of a binary tree

    given node i:
    * its left child: 2*i
    * its right child: 2*i + 1
    * its parent = i // 2

    See the Heap note for more info
    """

    def __init__(self, array: list = None):
        self.structure = array or list() # this is an array for the internal structure

    def heap_up(self) -> None:
        """
            Basically an internal function that sorts the heap
        :return:
        """
        index = len(self.structure) - 1
        parent_finder = lambda num: math.ceil(num / 2) - 1 if math.ceil(num / 2) > 0 else 0

        while 1:
            parent = parent_finder(index)
            if self.structure[index] > self.structure[parent]:
                self.structure[index], self.structure[parent], index = self.structure[parent], self.structure[index], parent

            if not parent:
                break

    def heap_down(self, index: int = None):
        index = index or 0

        def greater_child(i) -> int:
            """
                left child: 2 * i
                right childe: 2 * i + 1
            :param i:
            :return:
            """
            left_index, right_index, current_value = 2*i, 2*i + 1, self.structure[i]

            # case both present
            if right_index < len(self.structure):
                left_value, right_value = self.structure[left_index], self.structure[right_index]
                if current_value < left_value and current_value < right_value:
                    return left_index if left_value > right_value else right_index
                elif current_value < right_value:
                    return right_index
                return left_index
            # if only left present
            elif left_index < len(self.structure):
                left_value = self.structure[left_index]
                return left_index if left_value > current_value else i
            return i

        while 1:
            next_index = greater_child(index)
            self.structure[next_index], self.structure[index], index = self.structure[index], self.structure[next_index], next_index
            if next_index == index:
                break

    def heapify(self) -> None:
        for i in range(len(self.structure) - 1, -1, -1):
            self.heap_down(i)

    def insert(self, number: int) -> None:
        """
            insert must be appending the element to the end of the array, then bubble up
        :param number:
        :return:
        """

        # first, append to the array
        self.structure.append(number)
        self.heap_up()


    def isEmpty(self) -> bool:
        return not bool(self.structure)

    def pull(self) -> int:
        priority_value, self.structure[0] = self.structure[0], self.structure[-1]
        self.structure = self.structure[:-1]
        self.heap_down()
        return priority_value

    def peek(self) -> int:
        return self.structure[0]

def test_heap():
    my_heap = MaxHeap()
    # test insert
    my_heap.insert(3)
    assert my_heap.structure == [3]
    my_heap.insert(7)
    assert my_heap.structure == [7, 3]
    my_heap.insert(5)
    assert my_heap.structure == [7, 3, 5]
    my_heap.insert(100)
    assert my_heap.structure == [100, 7, 5, 3]

    # test isEmpty
    assert not my_heap.isEmpty()

    # test pull
    assert my_heap.pull() == 100
    assert not my_heap.isEmpty()
    assert my_heap.pull() == 7
    assert not my_heap.isEmpty()


if __name__ == "__main__":
    test_heap()
