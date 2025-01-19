ch = input()
while not (1 <= len(ch) <= 100):
	ch = input()

def freq(c,ch):
	F = 0
	for i in range(len(ch)):
		if c == ch[i]:
			F += 1
	return F

nbd = 0
R = ""

for i in range(len(ch)):
	F = freq(ch[i],ch)
	if F == 1:
		nbd += 1
	else:
		R += ch[i]
		F = freq(ch[i], R)
		if F == 1:
			nbd += 1

if nbd % 2 == 0:
	print("CHAT WITH HER!")
else: 
	print("IGNORE HIM!")

