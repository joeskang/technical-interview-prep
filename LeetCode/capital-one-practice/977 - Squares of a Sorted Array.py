"""
Runtime: 236 ms, faster than 59.78% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16 MB, less than 86.42% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:
    def sortedSquares(self, nums) -> list:
        left, right = 0, len(nums) - 1

        newarr = list(0 for _ in range(len(nums)))

        while left <= right:
            if -1 * nums[left] >= nums[right]:
                newarr[right-left] = nums[left] ** 2
                left += 1
            else:
                newarr[right-left] = nums[right] ** 2
                right -= 1

        return newarr

def test_solution():
    sol = Solution()
    assert sol.sortedSquares([-7, -4, 0, 2, 5]) == [0, 4, 16, 25, 49]

if __name__ == "__main__":
    test_solution()
