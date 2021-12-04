class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        """binary search"""

        left, right = 0, len(nums) - 1

        # edge cases
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        while left <= right:
            pivot = left + (right - left) // 2
            # TODO: continue from here

            if nums[pivot] == target:#  or (nums[pivot - 1] < target < nums[pivot + 1]):
                return pivot

            elif nums[pivot] < target:
                # if right == pivot + 1:
                #     return right
                left = pivot + 1

            else:
                # if left == pivot-1:
                #     return pivot
                right = pivot - 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    # print(sol.searchInsert([1,2,3,4,5,10], 8)) # expecting 5
    # print(sol.searchInsert([1, 2, 3, 4, 5, 10], -1)) # expecting 0
    # print(sol.searchInsert([1,2], 10)) # expecting 2
    print(sol.searchInsert([1,3,5,6], 2)) # expecting 1
