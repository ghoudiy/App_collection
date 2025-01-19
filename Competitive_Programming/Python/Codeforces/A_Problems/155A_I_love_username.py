m = int(input())

n = list(map(int, input().split()))


def minimum(T,bs):
	mini = T[0]
	for i in range(1,bs):
		if mini > T[i]:
			mini = T[i]
	return mini

def maximum(T,bs): 
	maxi = T[0]
	for i in range(1,bs): 
		if maxi < T[i]:
			maxi = T[i]
	return maxi

nba = 0
for i in range(1,m): 
	min1,max1 = minimum(n,i),maximum(n,i)
	if n[i] > max1: 
		nba += 1
	elif n[i] < min1:
		nba += 1

print(nba)
