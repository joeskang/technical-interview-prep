#!/bin/python3

"""
Time = 00:05:14
Date = June 08, 2022
"""

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    myd = {}
    # sorting is nlogn
    # two simultaneous for loops is still just n
    for i in a:
        if i in myd:
            myd[i] = False
        else:
            myd[i] = True

    for k, v in myd.items():
        if v:
            return k


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
