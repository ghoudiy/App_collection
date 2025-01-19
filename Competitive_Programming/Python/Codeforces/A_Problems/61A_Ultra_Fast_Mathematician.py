num = input()
num1 = input()

R = ""
for i in range(len(num)):
	if num[i] == "0" and num1[i] == "0":
		R += "0"
	elif num[i] == "0" and num1[i] == "1":
		R += "1"
	elif num[i] == "1" and num1[i] == "0":
		R += "1"
	else:
		R += "0"

print(R)
