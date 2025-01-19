#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
	# Write your code here
	max = candles[0]
	for i in range(1,candles_count):
		if max < candles[i]:
			max = candles[i]
	nb = 0
	for i in range(candles_count):
		if max == candles:
			nb += 1
	return nb
				
			
    

if __name__ == '__main__':

	candles_count = int(input().strip())

	candles = list(map(int, input().rstrip().split()))

	result = birthdayCakeCandles(candles)
