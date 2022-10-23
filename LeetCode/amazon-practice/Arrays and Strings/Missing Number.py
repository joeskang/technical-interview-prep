class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # first, naive approach O(nlogn)
        nums.sort()
        length = len(nums)

        for i in range(length + 1):
            if i not in nums:
                return i

        """
        # second, attempt at O(n)
        length = len(nums)
        max_exists = False
        direction = 0
        while type(direction) is not bool or direction < length:
            if nums[direction] == length:
                max_exists = True
                direction += 1
            else:
                temp = nums[direction]
                nums[direction] = True
                direction = temp

        for i in range(len(nums)):
            if type(nums[i]) is not bool:
                return i
        return length
        """
