'''
Runtime: 1090 ms, faster than 11.34% of Python3 online submissions for Maximum Subarray.
Memory Usage: 28.5 MB, less than 71.23% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # vals = []
        current = None
        max_ = None

        for i in range(len(nums)):
            if i == 0:
                current = max_ = nums[i]
            else:
                current = max(current + nums[i], nums[i])
                if current > max_:
                    max_ = current
        return max_