def number_solution(M,n):
	nb = 0
	for i in range(n):
		nb1 = 0
		for j in range(3):
			if M[i][j] == 1:
				nb1 += 1
		if nb1 >= 2:
			nb += 1
	return nb
			
n = int(input())
while not (1 <= n <= 1000):
	n = int(input())

M = []
for i in range(n):
	M.append(list(map(int, input().rstrip().split())))
nb = number_solution(M,n)
print(nb)











# n = int(input())
# while not (1 <= n <= 1000):
	# n = int(input())

# arr = []
# for i in range(n):
	# arr.append([0] * n)
	# for j in range(n):
		# arr[i][j] = int(input())
		# while not (0 <= arr[i][j] <= 1):
			# arr[i][j] = int(input())
# nb = 0
# for i in range(n):
	# nb1 = 0
	# for j in range(n):
		# if arr[i][j] == 1:
			# nb1 += 1
	# if nb1 >= 2:
		# nb += 1

# print(nb)
		
