"""
07/02/2022
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs traversal + cache
        is_land = {}  # keys: coordinate (tuple), values: Boolean
        island_count = 0

        def inner_dfs(x, y):

            if grid[x][y] != "1" or (x, y) in is_land:
                return

            is_land[(x, y)] = True

            # up
            if x > 0:
                inner_dfs(x - 1, y)
            # down
            if x < len(grid) - 1:
                inner_dfs(x + 1, y)
            # left
            if y > 0:
                inner_dfs(x, y - 1)
            # right
            if y < len(grid[0]) - 1:
                inner_dfs(x, y + 1)

        # nested for loop through the grid
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if (m, n) in is_land:
                    continue
                if grid[m][n] == "1":
                    island_count += 1
                    inner_dfs(m, n)

        return island_count