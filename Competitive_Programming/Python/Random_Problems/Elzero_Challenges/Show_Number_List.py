def Nums(L):
	# Remove duplicated elements
	i = 0
	while i < len(L):
		while L[i] in L[i+1:]:
			L.pop(L[i+1:].index(L[i]) + i + 1)
		if type(L[i]) == str:
			L.remove(L[i])
			i -= 1
		elif type(L[i]) in [bool, float]:
			L[i] = int(L[i])
		i += 1

	L = sorted(L, reverse=True)
	if len(L) % 2 == 1:
		print("\n".join(map(str, L)))
	else:
		for i in range(len(L) // 2 - 1):
			print(L[i] + L[len(L) - i - 1])
		print(L[i + 1] * L[len(L) // 2])
		
numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 8, 9]
Nums(numbers)

numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 3, 8, 9]
Nums(numbers)
