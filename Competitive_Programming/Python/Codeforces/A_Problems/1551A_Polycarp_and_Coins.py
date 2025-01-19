t = int(input())

ar = []
for _ in range(t): 
    ar.append(int(input()))

for i in range(t): 
    if ar[i] % 3 != 0: 
        print(ar[i] // 3 + (ar[i] % 3 == 1), ar[i] // 3 + (ar[i] % 3 == 2))
    else: 
        print(ar[i] // 3, ar[i] // 3)
