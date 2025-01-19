ar = list(map(int, input().split()))

nbm = 0

# From the internet
# L = []
# for l in ar:
# 	if l not in L:
# 		L.append(l)

# print(4 - len(L))

print(4 - len(set(ar)))


# Me

# def Freq(num,T):
	# F = 0
	# for i in range(4):
		# if num == T[i]:
			# F += 1
	# return F

# i = 0
# while i != 4:
	# F = Freq(ar[i],ar)
	# if F == 2:
		# nbm += 1
		# ar[i] = 0
	# elif F == 3:
		# print(2), exit()
	# elif F == 4:
		# print(3), exit()
	# i += 1
		
# print(nbm)


# def Freq(num,T):
	# F = 0
	# i = 0
	# while F < 2:
		# if num == T[i]:
			# F += 1
		# i += 1
	# if F > 1:
		# tmp = False
	# else:
		# tmp = True
	# return tmp
		

# for i in range(4):
	# ok = Freq(ar[i],ar)
	# if ok:
		# nbm += 1
		
# print(nbm)

