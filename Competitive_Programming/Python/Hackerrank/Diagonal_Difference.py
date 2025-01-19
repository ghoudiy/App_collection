#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
   # Write your code here
	S1 = 0
	S2 = 0
	for i in range(n):
		S1 += arr[i][i]
		S2 += arr[i][n-i-1]
	X = abs(S1 - S2)
	return X

			
if __name__ == '__main__':

	n = int(input().strip())

	arr = []

	for _ in range(n):
	  arr.append(list(map(int, input().rstrip().split())))

	result = diagonalDifference(arr)
