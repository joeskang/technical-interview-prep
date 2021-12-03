class Solution:
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    sol.search([1,2,3,4,5,10], 10)