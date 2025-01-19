#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    ch = "" 
    for i in range(n):
        space = " " * (n - i - 1)
        hash = "#" * (i + 1) 
        ch = space + hash
        print(ch)
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
