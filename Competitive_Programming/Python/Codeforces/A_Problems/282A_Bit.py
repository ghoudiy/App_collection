n = int(input())

x = 0
for i in range(n):
	ch = input()
	if "+" in ch:
		x += 1
	elif "-" in ch:
		x -= 1

print(x)
