t = int(input())

n = []
for i in range(t):
    n.append(int(input()))


for i in range(t): 
    if n[i] >= 3: 
        if n[i] % 2 != 0:
            nbd = n[i] // 2
        else: 
            nbd = n[i] // 2 - 1
        print(nbd)
    else: 
        print(0)
