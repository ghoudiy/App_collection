arr = []
for i in range(5):
	tmp = list(map(int, input().split()))
	arr.append(tmp)
	if 1 in tmp:
		l, c = i, tmp.index(1)
print(abs(l - 2) + abs(c - 2))

# input
"""
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
"""

# output
1