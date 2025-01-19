n = int(input())
while not (1 <= n <= 100):
	n = int(input())

for i in range(n):
	ch = input().lower()
	while not (1 <= len(ch) <= 100):
		ch = input().lower()
	if len(ch) > 10:
		ch = ch[0] + str(len(ch[1:len(ch)-1])) + ch[-1]
	print(ch)
 
