"""
Runtime: 32 ms, faster than 54.92% of Python3 online submissions for Summary Ranges.
Memory Usage: 14.2 MB, less than 48.85% of Python3 online submissions for Summary Ranges.
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = right = None
        past = None
        output = []
        for i in range(len(nums)):
            n = nums[i]
            if left is None:
                left = n

            elif n > past + 1:
                right = past

                output.append(f"{left}->{right}" if left != right else f"{right}")
                left = right = n

            if i == len(nums) - 1:
                right = n
                output.append(f"{left}->{right}" if left != right else f"{right}")

            past = n
        # last one
        # if left <= past:
        #     output.append(f"{left}->{right}" if left != right else f"{right}")

        return output