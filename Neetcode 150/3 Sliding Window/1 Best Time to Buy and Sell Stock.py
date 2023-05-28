import math
from collections import deque

def maxProfit(prices: list) -> int:

    # more storage, less speed
    min_stack, max_stack = [], deque()
    cur_min, cur_max = math.inf, -math.inf
    for i in range(len(prices)):
        cur_min = min(cur_min, prices[i])
        cur_max = max(cur_max, prices[len(prices) - (i+1)])

        min_stack.append(cur_min)
        max_stack.appendleft(cur_max)

    max_profit = 0

    for i in range(len(prices)):
        max_profit = max(max_stack[i] - min_stack[i], max_profit)
    return max_profit

def test1():
    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0

def test2():
    prices = [7, 1, 5, 3, 6, 4]
    assert maxProfit(prices) == 5

def test3():
    prices = [2,1,4]
    assert maxProfit(prices) == 3

if __name__ == "__main__":
    test1()
    test2()
    test3()