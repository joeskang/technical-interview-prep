class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # sacrifice space complexity for time complexity
        indices = []

        for i in range(len(nums)):
            # first, read through all the items in the list
            if nums[i] == 0:
                indices.append(i)

        left = 0
        for j in indices:
            while left < j:
                left += 1

