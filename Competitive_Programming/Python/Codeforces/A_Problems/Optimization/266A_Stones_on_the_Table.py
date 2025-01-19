n = int(input())
s = input()
nrm = 0
for i in range(n-1):
	if s[i] == s[i+1]:
		nrm += 1
print(nrm)
