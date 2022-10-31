"""
previously completed, reviewed

time: 00:06:16
date: 10/14/2022
"""

def twoSum(self, nums, target: int):
    difference = dict()

    for i, num in enumerate(nums):
        if (diff := target - num) in difference:
            return [difference[diff], i]
        difference[num] = i

    return []

