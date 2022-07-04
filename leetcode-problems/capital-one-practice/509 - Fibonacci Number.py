class Solution:
    def __init__(self):
        self.cache = dict()

    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        elif n not in self.cache:
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.cache[n]
        else:
            return self.cache[n]
