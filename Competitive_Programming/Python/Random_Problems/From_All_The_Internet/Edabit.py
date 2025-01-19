# Calculate damage

def damage(damage, speed, time):
	if damage >= 0 and speed >= 0:
		total = damage * speed
		if time == "minute":
			total *= 60
		elif time == "hour":
			total *= 3600
		return total
	else:
		return "invalid"
		
# Circle or Square

import math

def circle_or_square(rad, area):
	circumference_circle = 2 * math.pi * rad
	circumference_square = math.sqrt(area) * 4
	if circumference_circle > circumference_square:
		ok = True
	else:
		ok = False
	return ok

# End Corona!

def end_corona(recovers, new_cases, active_cases):
	day = int(active_cases / (recovers - new_cases)) + 1
	return day

# RegEx XV: Alternation

import re

pattern = "red flag|blue flag"

# Basic Calculator

def calculator(num1, operator, num2):
	if opeartor == "+":
		result = num1 + num2
	elif operator == "-":
		result = num1 - num2
	elif operator == "/":
		if num2 != 0:
			result = num1 / num2
		else:
			result = "Can't divide by 0!"
	elif operator == "*":
		result = num1 * num2
	return result

  # Other solutions:
  
	# if operator == '/' and num2 == 0:
		# return "Can't divide by 0!"
	# return eval('num1' + operator + 'num2')

	# try: 
		# return eval(str(n1)+operator+str(n2))
	# except ZeroDivisionError:
		# return "Can't divide by 0!"
