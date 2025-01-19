n = int(input())

M = []
for i in range(n):
	M.append(list(map(int, input().rstrip().split())))

pasn = M[0][0] + M[0][1]
max = pasn
for i in range(1,n):
	pasn -= M[i][0]
	pasn += M[i][1]
	if max < pasn:
		max = pasn

print(max)
		
	
