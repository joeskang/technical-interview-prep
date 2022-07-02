"""
Runtime: 80 ms, faster than 35.82% of Python3 online submissions for Flood Fill.
Memory Usage: 14.5 MB, less than 56.06% of Python3 online submissions for Flood Fill.
"""
class Solution:
    def __init__(self):
        self.visited = None
        self.color = None

    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if self.visited is None:
            self.visited = [[False for _ in range(len(image[0]))] for i in range(len(image))]
        if self.color is None:
            self.color = image[sr][sc]

        if not self.visited[sr][sc]:
            self.visited[sr][sc] = True

            if image[sr][sc] == self.color:
                image[sr][sc] = newColor

                # up first
                if sr > 0:
                    self.floodFill(image, sr-1, sc, newColor)
                # right
                if sc < len(image[0]) - 1:
                    self.floodFill(image, sr, sc +1, newColor)
                # left
                if sc > 0:
                    self.floodFill(image, sr, sc -1, newColor)
                # down
                if sr < len(image) - 1:
                    self.floodFill(image, sr +1, sc, newColor)

        return image

if __name__ == "__main__":
    sol = Solution()
    # ans = sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    ans = sol.floodFill([[0,0,0],[0,0,0]], 0,0,2)
    pass
