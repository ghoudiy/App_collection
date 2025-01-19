# Binzart
# Rasi Tflag
n,m = list(map(int, input().rstrip().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

def maximum(T):
	max = T[0]
	for i in range(1,len(T)): 
		if max < T[i]: 
			max = T[i]
	return max

L = set()
maxi = maximum(a)
for j in range(maxi,b[0]+1,maxi):
	for k in range(n):
		if j % a[k] == 0 and k <= n-1:
			l = 0
			ok = True
			while (ok == True) and (l < m): 
				if b[l] % j != 0: 
					ok = False
				l += 1
			if ok:
				L.add(j)

print(len(L))
"""
2 3
2 4
16 32 96
"""

# ~ k in range(i+1,n):
		# ~ print("[j,a[k]]=",j,a[k])
		# ~ if j % a[k] == 0: 
			# ~ for l in range(m): 
				# ~ print("[j,b[l]]=",j,b[l])
				# ~ if j % b[l] == 0: 
					# ~ L.append(j)
