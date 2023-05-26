"""
https://leetcode.com/problems/binary-search/
704. Binary Search
"""

def search(nums: list, target: int) -> int: # returns the index

    l,r = 0, len(nums) - 1

    while l < r:
        m = l + ((r - l) // 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    for index in (l, r):
        if nums[index] == target:
            return index
    return -1

def test1():
    my_array = [1, 3, 4, 5, 9, 10]
    assert search(my_array, 1) == 0
    # assert search(my_array, 10) == 5

if __name__ == "__main__":
    test1()

