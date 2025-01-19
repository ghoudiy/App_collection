Limak, Bob= map(int, input().rstrip().split())

nby = 0
while Limak <= Bob:
	Limak *= 3
	Bob *= 2
	nby += 1
print(nby)
