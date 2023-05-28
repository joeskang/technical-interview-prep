"""
https://leetcode.com/problems/sort-an-array/

LeetCode # 912

** Insertion Sort fails because Time Limit Exceeded
"""

def sortArray(nums: list[int]) -> list[int]:

    for i in range(len(nums)):
        j = i - 1

        while j >= 0 and nums[j+1] < nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1

    return nums

def test_1():
    my_arr = list([5, 2, 1, 3, 9])
    assert sortArray(my_arr) == sorted(my_arr)


if __name__ == "__main__":
    test_1()