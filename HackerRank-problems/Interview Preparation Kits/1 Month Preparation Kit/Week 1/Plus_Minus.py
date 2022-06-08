#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos_count = 0
    neg_count = 0
    # zero count is the difference between total and the parts

    for num in arr:
        # negative
        if num < 0:
            neg_count += 1

        # positive
        elif num > 0:
            pos_count += 1

        # zeros

    # print positive ratio
    print(str("{:.6f}").format(pos_count / len(arr)))

    # print negative ratio
    print(str("{:.6f}").format(neg_count / len(arr)))

    # print zeros ratio
    print(str("{:.6f}").format((len(arr) - pos_count - neg_count) / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
