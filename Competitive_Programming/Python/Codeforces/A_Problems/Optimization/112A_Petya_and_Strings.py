s = input().lower()
s1 = input().lower()
if s == s1:
	print(0)
elif s > s1:
	print(1)
else:
	print(-1)
	
# input
"""
aaaa
aaaA

abs
Abz

abcdefg
AbCdEfF
"""

# output
0
-1
1
