
class Solution:
    def __init__(self):
        self.cache = {}

    def minCostClimbingStairs(self, cost:list) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        if len(cost) == 1:
            return cost[0]
        if len(cost) < 1:
            return 0
        left, right = len(cost) - 2, len(cost) - 1
        if right not in self.cache:
            self.cache[right] = cost[right] + min(self.minCostClimbingStairs(cost[0:right]), self.minCostClimbingStairs(cost[0:right-1]))
            return self.cache[right]
        if left not in self.cache:
            self.cache[left] = cost[left] + min( self.minCostClimbingStairs(cost[0:left]), self.minCostClimbingStairs(cost[0:left-1]))
            return self.cache[left]
        return min(self.cache[right], self.cache[left])

if __name__ == "__main__":
    sol = Solution()
    # ans = sol.minCostClimbingStairs([10, 15, 20])
    ans = sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
    pass
