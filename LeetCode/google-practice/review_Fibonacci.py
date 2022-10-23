"""
redoing dynamic programming Fibonacci with memoization
"""

class Solution:

    def __init__(self):
        self.cache = {}

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n not in self.cache:
                self.cache[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
            return self.cache[n]


if __name__ == "__main__":
    sol = Solution()
    num = 8
    print(f"the fibonacci of {num} is {sol.fibonacci(num)}")

