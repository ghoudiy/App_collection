#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
	 # Write your code here
	 S = 0
	 for i in range(len(ar)):
		  S += ar[i]
	 return S

if __name__ == '__main__':
	 fptr = open(os.environ['OUTPUT_PATH'], 'w')

	 ar_count = int(input().strip())

	 ar = list(map(int, input().rstrip().split()))

	 result = simpleArraySum(ar)

	 fptr.write(str(result) + '\n')

	 fptr.close()

# [Solved]
