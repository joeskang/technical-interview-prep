#!/bin/python3


import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here

    # null array case
    if len(s) < m:
        return 0

    curr_sum = 0
    count = 0
    for i in range(len(s)):

        # the start of the contigs
        if i < m:
            curr_sum += s[i]
            if i < m - 1:
                continue
        # else, we've gone past the start
        else:
            # subtract the first
            curr_sum -= s[i - m]

            # add the current
            curr_sum += s[i]

        # check to see if match
        if curr_sum == d:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
