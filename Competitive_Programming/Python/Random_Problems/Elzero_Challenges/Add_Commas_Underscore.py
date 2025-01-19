def add_commas_and_underscore(num):
	num = str(num)

	if len(num) >= 4:
		num = num[:-3] + "_" + num[-3:]
	if len(num) > 6:
		i = len(num) - 5
		while len(num[:i]) >= 3:
			i -= 3
			num = num[:i+1] + "," + num[i+1:]

		return num

	return num

# Testing Ouput
print(add_commas_and_underscore(120)) # 120
print(add_commas_and_underscore(1530)) # 1_530
print(add_commas_and_underscore(120510650)) # 120,510_650
print(add_commas_and_underscore(510650480910)) # 510,650,480_910
print(add_commas_and_underscore(12069057014032)) # 12,069,057,014_032
print(add_commas_and_underscore(23497832489734209873249082734098)) # 12,069,057,014_032