"""

"""

class Solution:
    def __init__(self):
        self.cache = dict()
    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n not in self.cache:
            self.cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return self.cache[n]
        else:
            return self.cache[n]