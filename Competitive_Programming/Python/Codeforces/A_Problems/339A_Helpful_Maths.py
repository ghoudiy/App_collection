ch = input()

L = []
for i in range(0,len(ch),2):
	L.append(ch[i])

ok = False
while ok == False:
	ok = True
	for i in range(len(L)-1):
		if L[i] > L[i+1]:
			Aux = L[i+1]
			L[i+1] = L[i]
			L[i] = Aux
			ok = False

print("+".join(L))
