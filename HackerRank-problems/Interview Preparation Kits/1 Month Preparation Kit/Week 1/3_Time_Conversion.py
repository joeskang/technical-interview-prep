#!/bin/python3
"""
forgot to time this one
Date = June 07, 2022
"""

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    meridian = s[-2]

    if meridian == "P" and hour != 12:
        hour += 12

    elif meridian == 'A' and hour == 12:
        hour = 0

    hour = "0" + str(hour) if hour < 12 else str(hour)
    return_string = hour + s[2:-2]
    return return_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
