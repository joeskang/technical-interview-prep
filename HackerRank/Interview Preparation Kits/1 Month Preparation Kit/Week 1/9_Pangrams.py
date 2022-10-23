#!/bin/python3
"""
Time = 00:03:45
Date = June 08, 2022
"""

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alpha_d = {}
    # if letter was present then value = true
    for _ in range(26):
        alpha_d[chr(ord('a') + _)] = False
    for c in s:
        alpha_d[c.lower()] = True
    for k, v in alpha_d.items():
        if not v:
            return "not pangram"
    return "pangram"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
