n = int(input())
U = 1
i = 1
for i in range(2, n):
	if U + i >= n:
		i -= 1
		break
	U += i
	n -= U
 
print(i)
