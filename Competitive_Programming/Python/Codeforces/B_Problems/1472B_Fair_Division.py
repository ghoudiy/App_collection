t = int(input()) * 2

arr = []
for _ in range(t): 
	arr.append(list(map(int, input().split())))
	
for i in range(0,t-1,2): 
	n = arr[i][0]
	i += 1
	ar = arr[i]
	F1 = ar.count(1)
	F2 = ar.count(2)
	two = lambda num: "YES" if num % 2 == 0 else "NO"
	if F1 == 0: 
		print(two(F2))
	elif F2 == 0: 
		print(two(F1))
	else: 
		S = sum(ar) / 2
		if S == int(S):
			print("YES")
		else: 
			print("NO")
		
		