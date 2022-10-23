# Basically same problem as fibonacci
"""
Runtime: 32 ms, faster than 54.63% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.1 MB, less than 91.03% of Python3 online submissions for Climbing Stairs.
"""

class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        elif n not in self.cache:
            self.cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
            return self.cache[n]
        else:
            return self.cache[n]