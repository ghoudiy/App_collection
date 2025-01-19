x = 0
for _ in range(int(input())):
	x += 1 if input().find("+") != -1 else -1
print(x)

# input
"""
1
++X
2
X++
--X
"""

# output
1
0
