n, k = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

nbp = 0
for i in range(n):
	if a[k-1] == 0 and a[i] == a[k-1]:
		nbp += 0
	elif a[k-1] <= a[i]:
		nbp += 1
	else:
		nbp += 0
print(nbp)

# Not Me
