"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

"""

def findMin(nums: list) -> int:
    import math

    minimum = math.inf

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = nums[mid]
        minimum = min(minimum, mid_value)

        if mid_value < nums[right]:
            right = mid - 1
        else:
            left = mid + 1

    return minimum

def test_1():
    array = [3,4,5,1,2]

    assert findMin(array) == 1


def test_2():
    array = [11, 13, 15, 17]
    assert findMin(array) == 11


if __name__ == "__main__":
    test_1()
    test_2()
