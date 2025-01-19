n,t = map(int, input().split())
s = input()

for _ in range(t):
	i = 0
	while i < len(s) - 1: 
		if s[i] == "B" and s[i+1] == "G": 
			s = s[:i] + "GB" + s[i+2:]
			i += 1
		i += 1
print(s)