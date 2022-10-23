"""
Runtime: 108 ms, faster than 14.00% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.8 MB, less than 5.44% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
"""

class Solution:
    def twoSum(self, numbers, target: int):
        """going to move from both left and right until closed in"""
        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1



def test_solution():
    sol = Solution()
    assert sol.twoSum([1,3,4,5,6], 10) == [3, 5]
    assert sol.twoSum([2,7,8, 19, 21], 23) == [1, 5]
    assert sol.twoSum([-1000, -1, 0, 1], 1) == [3,4]

if __name__ == "__main__":
    test_solution()