n = int(input())
while not (1 <= n <= 50):
	n = int(input())

ch = input()

L = [0]
for i in range(1,len(ch)):
	if ch[-i] == ch[-i-1]:
		L.insert(0,1)

nbm = 0
for num in L:
	nbm += num
	
print(nbm)
