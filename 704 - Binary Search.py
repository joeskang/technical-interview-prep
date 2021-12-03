"""
RESULTS:

Runtime: 244 ms, faster than 44.07% of Python3 online submissions for Binary Search.
Memory Usage: 15.7 MB, less than 30.54% of Python3 online submissions for Binary Search.

"""

class Solution:
    def __init__(self):
        pass

    def search(self, nums: list, target: int) -> int:
        offset = 0

        while 1:

            # take center
            # if odd number of items, then give preference to second half
            half_index = int(len(nums) / 2)
            mid = nums[half_index]

            # check the item at the middle, if matching target, return
            if mid == target:
                return offset + half_index

            else:
                # if the array is size one and it doesn't match, then it wasn't here
                if len(nums) == 1:
                    return -1

                # check the last of the first half
                if mid > target:
                    nums = nums[:half_index]

                # check the first of the second half
                # elif nums[half_index+1] < target:
                else:
                    nums = nums[half_index:]
                    offset += half_index


def test_search():
    sol = Solution()
    assert sol.search(list(range(5)), 3) == 3
    assert sol.search([1,2,3,4,5,10], 10) == 5
    assert sol.search([-1,0,3,5,9,12], 2) == -1
    assert sol.search([2,5], 2) == 0
