n = int(input())

arx = list(map(int, input().split()))
ary = list(map(int, input().split()))

# L = set(arx[1:] + ary[1:])
# print("I become the guy." if len(L) == n else "Oh, my keyboard!")

# Method 2

def freq(num,T,N):
	F = 0
	for i in range(n):
		if num == T[i]:
			F += 1
	return F 

for i in range(1,arx[0]+1):
	# Lycee
	# l = len(L)
	# F = freq(arx[i],ary,l)
	# if F == 1:
		# ary.append(arx[i]) # L += str(arx[i])
	if arx[i] not in ary[1:]:
		ary.append(arx[i])

if len(ary[1:]) == n:
	print("I become the guy.")
else:
	print("Oh, my keyboard!")		
