k, n, w = map(int, input().rstrip().split())

money = 0
for i in range(1,w+1):

	money += (k * i)

print(money - n if (money - n) > 0 else 0 )
