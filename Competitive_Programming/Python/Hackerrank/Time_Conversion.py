#!/bin/python3

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
  hh = s[:2]
  if s[8:] == "AM" and hh == "12":
    hh = "00"
  if s[8:] == "PM" and hh != "12":
    hh = str(int(hh) + 12)
  ch = hh + s[2:8]
  return ch 

if __name__ == '__main__':

  s = input()

  result = timeConversion(s)



  print(result)
