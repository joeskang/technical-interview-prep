#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    # edge case:
    if n == 0:
        return 1

    ## the following is a naive implementation:
    # counts = 0
    # for i in range(n+1):
    #     if n + i == n^i:
    #         counts += 1
    # return counts

    # however, if you think about it, binary XOR is very similar to addition
    # actually, all you really need to do to solve is count the number of zeros in the binary
    # then, return 2 to the power of the zeros count
    mys = str(bin(n))[2:]
    return 2 ** mys.count('0')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
