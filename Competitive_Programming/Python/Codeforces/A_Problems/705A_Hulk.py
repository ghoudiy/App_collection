n = int(input())

R = ""

feelings = ["hate", "love"]
j = -1
for i in range(n):
	j += 1
	if j >= 2:
		j = 0
	R += " I " + feelings[j] + " that"

print(R[1:-5] + " it")
	
