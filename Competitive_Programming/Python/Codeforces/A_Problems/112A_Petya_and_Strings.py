def saisie(bi,bs):
	c = input()
	while not (bi <= len(c) <= bs):
		c = input()
	return c

ch = saisie(1,100)
ch1 = saisie(1,100)

while len(ch) != len(ch1):
	ch = saisie(1,100)
	ch1 = saisie(1,100)

if ch.lower() > ch1.lower():
	print(1)

elif ch.lower() < ch1.lower():
	print(-1)

else:
	print(0)

