#!/bin/python3
"""
Time = 00:02:49
Date = June 08, 2022
"""

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()
    if len(arr) % 2:
        # the length is odd so return middle number
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
