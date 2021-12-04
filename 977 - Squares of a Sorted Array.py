class Solution:
    def sortedSquares(self, nums) -> list:
        left, right = 0, len(nums) - 1

        # square each element
        for i in range(len(nums)):
            nums[i] = i ** 2

        while left < right:
            square = nums[left]
            while 1:
                if nums[right] > square:
                    right -= 1
                else:
                    nums = nums[1:right] + [square] + nums[right:]
                    break

        # TODO: continue


