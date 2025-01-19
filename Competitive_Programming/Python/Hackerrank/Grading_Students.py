#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
	# Write your code here
	for i in range(grades_count):
		if grades[i] >= 38:
			rounded = grades[i]
			for j in range(3):
				if rounded % 5 != 0:
					rounded += 1
			if rounded - grades[i] < 3:
				grades[i] += (rounded - grades[i])
	return grades
          
if __name__ == '__main__':

	grades_count = int(input().strip())

	grades = []

	for _ in range(grades_count):
			grades_item = int(input().strip())
			grades.append(grades_item)

	result = gradingStudents(grades)
	print(result)
