class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # sacrifice space complexity for time complexity
        indices = []

        for i in range(len(nums)):
            # first, read through all the items in the list
            # get the non-zeros
            if nums[i] != 0:
                indices.append(i)
        # indices.append(len(nums) - 1)

        left = 0
        for index in indices:
            nums[left] = nums[index]
            left += 1
        for j in range(len(nums) - len(indices)):
            nums[-j - 1] = 0

        """how to perform swap operation in Python"""
        y = 1
        x=2
        x, y = y, x




        # moving non-zeros
        left = 0
        # for j in range(len(indices)):
        #     # j + 1 becomes the offset for left
        #     cur = indices[j]
        #     while left < cur:
        #         nums[left] = nums[left + j + 1]
        #         left += 1
        #
        #     # need to skip the zero
        #     left += 1

        """there should be a better way to do it while accessing each item just once"""

        # moving zeros
        # for j in range(len(indices)):
        #     nums[-j-1] = 0

        # for debugging purposes
        return nums

def test_solution():
    sol = Solution()
    assert sol.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert sol.moveZeroes([0]) == [0]
    assert sol.moveZeroes([0, 0, 1, 1, 0]) == [1, 1, 0, 0, 0]

if __name__ == "__main__":
    test_solution()