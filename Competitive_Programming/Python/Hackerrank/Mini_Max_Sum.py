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
    min = 0 
    max = 0
    for i in range(4): 
        min += arr[i]
        i += 1
        max += arr[i]
    
    for i in range(4):
        S = 0 
        for j in range(4):
            if i == j: 
                j += 1
                S += arr[j] 
        if S > max : 
            max = S 
        if S < min : 
            min = S
    print(min, max)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
