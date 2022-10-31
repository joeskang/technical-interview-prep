
"""
Runtime: 63 ms, faster than 20.53% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14 MB, less than 75.08% of Python3 online submissions for Implement Stack using Queues.

date: 10/30/2022
"""
from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            temp = self.queue.popleft()
            self.queue.append(temp)
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
