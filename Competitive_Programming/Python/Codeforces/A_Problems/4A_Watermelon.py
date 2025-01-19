w = int(input())
while not (1 <= w <= 100):
	w = int(input())
ok = False
for i in range(1,w):
	if i % 2 == 0: 
		if w % i == 0:
			ok = True
	
if ok == True:
	print("YES")
else:
	print("NO")
