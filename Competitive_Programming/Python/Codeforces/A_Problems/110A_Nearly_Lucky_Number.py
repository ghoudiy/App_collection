n = int(input())

ch = str(n)

nbl = 0

for i in range(len(ch)):
	if ch[i] == "7" or ch[i] == "4":
		nbl += 1

if nbl == 7 or nbl == 4:
	print("YES")
else:
	print("NO")
