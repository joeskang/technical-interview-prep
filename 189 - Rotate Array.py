class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        size = len(nums)

        while left < k:
            # flip flop
            register = nums[left + k]
            nums[left + k] = nums[left]
            nums[(left + 2 * k) % (size-1)] = register
            left += 1

def test_solution():
    sol = Solution()
    assert

