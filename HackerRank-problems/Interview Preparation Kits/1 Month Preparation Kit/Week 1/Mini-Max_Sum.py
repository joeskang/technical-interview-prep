#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    the_sum = sum(arr)
    mini_sum = the_sum - max(arr)
    max_sum = the_sum - min(arr)
    print(mini_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
