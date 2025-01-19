n = int(input())
if n % 100 != 0: 
	print((5 ** (n % 100)) % 100)
else: 
	while n % 100 == 0: 
		n //= 10
	print((5 ** (n % 100)) % 100)
