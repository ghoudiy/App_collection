for _ in range(int(input())):
	a, b = sorted(map(int, input().split()))
	print(max(2*a,b) ** 2)
	
