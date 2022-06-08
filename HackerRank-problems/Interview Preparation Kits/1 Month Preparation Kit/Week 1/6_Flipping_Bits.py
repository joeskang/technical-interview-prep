#!/bin/python3

"""
Time: 00:13:51
Date: June 08, 2022

while I know that Python has the built-in bin() function,
I decided to write my own crude version of it for the spirit of
coding exercises
"""

import math
import os
import random
import re
import sys


#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here

    # decided to write binary conversion instead of relying on bin()
    def int_to_bit(num):
        bit_stack = []
        while num > 0:
            bit_stack.append(num % 2)
            num //= 2

        return bit_stack

    def bit_to_int(binary):
        num = 0
        binary = binary[::-1]
        exp = 0
        for c in binary:
            num += 2 ** exp * int(c)
            exp += 1
        return num

    bit_stack = int_to_bit(n)
    return_string = ""
    for i in range(32 - len(bit_stack)):
        return_string += "1"
    while bit_stack:
        num = bit_stack.pop()
        return_string += "0" if num else "1"

    return bit_to_int(return_string)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
