# n = int(input())

def int_sqrt(x):
	L = 1
	R = x
	while R >= L:
		mid = L + ((R - L) // 2)
		if mid * mid == x:
			return mid
		elif mid * mid < x:
			L = mid + 1
		else:
			R = mid - 1
	return -1
	
from time import time
for i in range(17):
	print("-" * 50)
	n = i
	print(f"{n = }")
	s = time()
	a = int_sqrt(n)
	e1 = time() - s
	print(f"{(e1):.17f} Binary search {a}")
	s = time()
	a = n ** 0.5
	e2 = time() - s
	print(f"{(e2):.17f} power of 0.5 {a}")
	from math import sqrt
	s = time()
	a = sqrt(n)
	e3 = time() - s
	print(f"{(e3):.17f} sqrt function {a}")
	
	if e1 < e2 and e1 < e3:
		print("Binary search is faster")
	elif e2 < e1 and e2 < e3:
		print("Power of 0.5 is faster")
	elif e3 < e1 and e3 < e2:
		print("Sqrt function is faster")
