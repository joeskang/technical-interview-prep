#!/bin/python3
"""
Time = 00:05:07
Date = June 08, 2022
"""

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    # find the length
    length = len(arr[0])

    diag_a = diag_b = 0
    for i in range(length):
        diag_a += arr[i][i]
        diag_b += arr[i][length - i - 1]

    return abs(diag_a - diag_b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
