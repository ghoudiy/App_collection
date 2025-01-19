M = [] 
for i in range(5):
	M.append(list(map(int, input().rstrip().split())))

ok = False
i = 0
j = 0
if M[i][j] == 1:
	ok = True
while M[i][j] != 1 and ok == False:
	j += 1
	if j == 5:
		i += 1
		j = 0
	if M[i][j] == 1:
		ok = True

i += 1
j += 1
nbm = 0
if i != 3:
	i = abs(i - 3)
	nbm += i
if j != 3:
	j = abs(j - 3)
	nbm += j

print(nbm)

	
