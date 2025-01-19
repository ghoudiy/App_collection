n = int(input())
print(n // 5 if n % 5 == 0 else n // 5 + 1)

exit()
x = int(input())

if x > 10 and x % 5 != 0:
	steps = x // 5 + 1
	print(steps)

else:
	L = []
	for i in range(1,6):
		steps = x / i
		if steps - int(steps) == 0:
			L.append(steps)

	ok = False
	while ok == False:
		ok = True
		for i in range(len(L)-1):
			if L[i] > L[i+1]:
				Aux = L[i+1]
				L[i+1] = L[i]
				L[i] = Aux
				ok = False
	print(L[0])



# x = int(input())

# L = []
# for i in range(1,6):
# 	if x > 10 and x % 5 != 0:
# 		steps = x // 5 + 1
# 		print(steps)
# 		exit()
# 	else:
# 	steps = x / i
# 	if steps - int(steps) == 0:
# 		L.append(steps)

# ok = False
# while ok == False:
# 	ok = True
# 	for i in range(len(L)-1):
# 		if L[i] > L[i+1]:
# 			Aux = L[i+1]
# 			L[i+1] = L[i]
# 			L[i] = Aux
# 			ok = False
			
# print(int(L[0]))


