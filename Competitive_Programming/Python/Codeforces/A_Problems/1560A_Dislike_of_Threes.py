t = int(input())

ar = []
for _ in range(t): 
    ar.append(int(input()))

for i in range(t): 
    j = 0
    c = 0
    while (j != ar[i]): 
        j += 1
        c += 1
        while (c % 3 == 0) or (c % 10 == 3): 
            c += 1
    print(c)