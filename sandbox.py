class Solution:
    def maxArea(self, height) -> int:
        volumes = {}
        left, right = 0, len(height) - 1
        volume = (right - left) * min(height[left], height[right])
        volumes[volume] = (left, right)
        while left < right:
            if height[right] < height[left]:

                right -= 1

            else:
                left += 1

            volume = (right - left) * min(height[left], height[right])

            volumes[volume] = (left, right)

        return max(list(volumes.keys()))


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))