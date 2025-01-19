ch = input()

nbu = 0
nbl = 0
for i in range(len(ch)):
	if ch[i] == ch[i].upper():
		nbu += 1
	else:
		nbl += 1

if nbu > nbl:
	print(ch.upper())
else:
	print(ch.lower())
