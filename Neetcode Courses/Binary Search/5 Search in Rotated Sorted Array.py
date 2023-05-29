
"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

def search(nums: list, target: int) -> int:

    left, right = 0, len(nums) - 1
    # edge case
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right

    while left <= right:
        mid = (left + right ) // 2
        mid_value = nums[mid]

        if mid_value == target:
            return mid

        if mid_value < target < nums[right] or mid_value > nums[right] > target:
            left = mid + 1

        # elif nums[left] < target < mid_value or target < mid_value < nums[left]:
        else:
            right = mid - 1

    return -1

def test_1():
    assert search([4,5,6,7,0,1,2], 0) == 4

def test_2():
    assert search([4,5,6,7,0,1,2], 3) == -1

def test_3():
    assert search([1], 0) == -1

def test_4():
    assert search([1,3], 3) == 1

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
