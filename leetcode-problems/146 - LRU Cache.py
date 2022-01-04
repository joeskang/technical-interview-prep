# NOT MY SOLUTION

"""
Runtime: 1366 ms, faster than 14.99% of Python3 online submissions for LRU Cache.
Memory Usage: 75.2 MB, less than 93.88% of Python3 online submissions for LRU Cache.
"""
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)