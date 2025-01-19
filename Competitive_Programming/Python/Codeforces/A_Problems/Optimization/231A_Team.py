noi = 0
for i in range(int(input())):
	ar = map(int, input().split())
	noi += 1 if sum(ar) >= 2 else 0
print(noi)

# input
"""
3
1 1 0
1 1 1
1 0 0
2
1 0 0
0 1 1
"""

# output
2
1
