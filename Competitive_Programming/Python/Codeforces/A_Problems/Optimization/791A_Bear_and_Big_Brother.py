a, b = map(int, input().split())
nry = 0
while a <= b:
	a *= 3
	b *= 2
	nry += 1
print(nry)