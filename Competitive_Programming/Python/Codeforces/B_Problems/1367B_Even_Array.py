t = int(input()) * 2

arr = []
for _ in range(t):
    arr.append(list(map(int, input().split())))
    
def good(T): 
	nre = 0
	for i in range(0,len(T),2): 
		if T[i] % 2 == 1:
			nre += 1
	nro = 0
	for j in range(1,len(T),2):
		if T[j] % 2 == 0:
			nro += 1
	return nre,nro

    
for i in range(0,t-1,2): 
	n = arr[i][0]
	i += 1
	ar = arr[i]
	even,odd = good(ar)
	if even == odd:
		print((even + odd) // 2)
	else: 
		print(-1)
		