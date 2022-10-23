#!/bin/python3
"""
forgot to time this one

Date = June 08, 2022
"""

import math
import os
import random
import re
import sys


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # Write your code here
    myd = {}
    for s in strings:
        if s not in myd:
            myd[s] = 1
        else:
            myd[s] += 1

    array = []
    for q in queries:
        array.append(myd[q] if q in myd else 0)

    return array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
