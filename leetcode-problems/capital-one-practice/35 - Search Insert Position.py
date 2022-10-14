"""
Runtime: 44 ms, faster than 92.60% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.2 MB, less than 24.36% of Python3 online submissions for Search Insert Position.
"""

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        """binary search"""

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                return pivot

            elif nums[pivot] < target:
                left = pivot + 1

            else:
                right = pivot - 1

        return left


def test_solution():
    sol = Solution()
    assert sol.searchInsert([1,2,3,4,5,10], 8) == 5
    assert sol.searchInsert([1, 2, 3, 4, 5, 10], -1) == 0
    assert sol.searchInsert([1,2], 10) == 2
    assert sol.searchInsert([1,3,5,6], 2) == 1
