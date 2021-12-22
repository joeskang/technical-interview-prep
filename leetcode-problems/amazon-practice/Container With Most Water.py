class Solution:
    def maxArea(self, height) -> int:
        left, right = 0, len(height) - 1
        max_volume = 0

        val_dict = {}
        for i in range(len(height)):
            val_dict[height[i]] = i

        while left < right:
            x = max()