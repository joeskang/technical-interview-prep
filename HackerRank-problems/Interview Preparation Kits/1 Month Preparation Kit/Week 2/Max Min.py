#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # null edge cases
    if k == 0 or not arr:
        return 0

    # Write your code here
    diffs = []
    # 1. sort
    arr.sort()

    # another null edge case
    if len(arr) <= k:
        return arr[-1] - arr[0]

    # 2. calculate differences
    for i in range(len(arr) - 1):
        diffs.append(arr[i + 1] - arr[i])

    least_bias = math.inf
    # 3. sliding min sum
    left = right = 0
    for left in range(len(arr) - k + 1):
        right = left + k - 1
        least_bias = min(least_bias, arr[right] - arr[left])
    # curr_sum = 0
    # while right < len(diffs) - 1:
    #     if right == 0:
    #         while right < k - 1:
    #             curr_sum += diffs[right]
    #             right += 1
    #     else:
    #         right += 1
    #         curr_sum -= diffs[left]
    #         curr_sum += diffs[right]
    #         left += 1
    #
    #     # min sum
    #     least_bias = min(least_bias, curr_sum)

    return least_bias


if __name__ == '__main__':
    maxMin(5, [4504,
1520,
5857,
4094,
4157,
3902,
822,
6643,
2422,
7288,
8245,
9948,
2822,
1784,
7802,
3142,
9739,
5629,
5413,
7232])
