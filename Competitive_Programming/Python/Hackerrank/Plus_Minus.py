#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pv = 0 
    nv = 0 
    z = 0
    for i in range(n): 
        if arr[i] > 0: 
            pv += 1
        elif arr[i] < 0:
            nv += 1
        else: 
            z += 1
    pv /= n
    nv /= n
    z /= n 
    print("%.6f"% pv)
    print("%.6f"% nv)
    print("%.6f"% z)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
