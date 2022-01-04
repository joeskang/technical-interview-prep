# not my solution
"""
Runtime: 103 ms, faster than 29.31% of Python3 online submissions for Min Stack.
Memory Usage: 18.5 MB, less than 18.08% of Python3 online submissions for Min Stack.
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return

        current_min = self.stack[-1][1]
        self.stack.append((val, min(current_min, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]