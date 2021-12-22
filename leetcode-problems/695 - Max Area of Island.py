"""
Runtime: 144 ms, faster than 61.09% of Python3 online submissions for Max Area of Island.
Memory Usage: 17.2 MB, less than 31.47% of Python3 online submissions for Max Area of Island.
"""
class Solution:
    def __init__(self):
        self.visited = None

    def maxAreaOfIsland(self, grid) -> int:
        if self.visited is None:
            self.visited = [[False for _ in range(len(grid[0]))] for i in range(len(grid))]

        def dfs(r, c, sum):

            if not self.visited[r][c]:

                self.visited[r][c] = True
                if grid[r][c] == 1:
                    sum += 1

                    if r < len(grid) - 1:
                        sum = dfs(r+1, c, sum)

                    if c < len(grid[0]) - 1:
                        sum = dfs(r, c+1, sum)

                    if r > 0:
                        sum = dfs(r-1, c, sum)

                    if c > 0:
                        sum = dfs(r, c-1, sum)

            return sum

        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not self.visited[i][j]:
                    output = max(dfs(i, j, 0), output)

                else:
                    pass


        return output

if __name__ == "__main__":
    sol = Solution()
    res = sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    pass
