#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
  
    maxi = scores[0]
    mini = scores[0]
    nbx = 0
    nbi = 0
    for i in range(1,n): 
        if maxi < scores[i]:
            nbx += 1
            maxi = scores[i]
        if mini > scores[i]:
            nbi += 1
            mini = scores[i]
    L = [nbx, nbi]
    return L        
    



if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)

