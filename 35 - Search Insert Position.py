class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        """binary search"""

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] == target or (nums[pivot - 1] < target < nums[pivot + 1]):
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return right


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,2,3,4,5,10], 8))