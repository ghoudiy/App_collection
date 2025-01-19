t = int(input())

ar = [0] * t
for i in range(t): 
    ar[i] = int(input())

for i in range(t): 
    S = (ar[i] % 10 - 1) * 10
    j = 0
    for i in range(len(str(ar[i]))): 
        j += 1
        S += j
    print(S)    