n, k = map(int, input().split())
ar = list(map(int, input().split()))

nop = 0
for score in ar:
	if score >= ar[k-1] and score > 0:
		nop += 1
print(nop)

# input
"""
8 5
10 9 8 7 7 7 5 5
4 2
0 0 0 0
"""

# ouput
6
0
