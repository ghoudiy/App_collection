from math import sqrt

n,m = map(int, input().split())

def Prime(n): 
	F = 1
	i = 2
	while (F == 1) and (i <= int(sqrt(n)) + 1):
		F += 1 if n % i == 0 else 0
		i += 1
	return F == 1
	
n += 1
while Prime(n) == False: 
	n += 1
print("YES" if n == m else "NO")