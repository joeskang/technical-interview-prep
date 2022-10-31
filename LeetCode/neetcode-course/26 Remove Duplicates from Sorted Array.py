"""
Runtime: 76 ms, faster than 99.83% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 66.37% of Python3 online submissions for Remove Duplicates from Sorted Array.

date: 10/30/2022
"""

import math

def solution(nums:list):
    past_num = math.inf
    store_index = 0
    count = 0
    for index in range(len(nums)):
        if (val := nums[index]) != past_num:
            nums[index] = None
            nums[store_index] = val
            store_index += 1
            past_num = val
            count += 1
        if index > store_index:
            nums[index] = None
    return count

def test():
    nums = [1,1,2]
    print(solution(nums))

if __name__ == "__main__":
    test()