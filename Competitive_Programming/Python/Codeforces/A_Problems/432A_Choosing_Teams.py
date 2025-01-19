n,k = map(int,input().split())

ar = list(map(int,input().split()))

nbp = 0
nbt = 0
for i in range(n): 
    if ar[i] + k <= 5: 
        nbp += 1
    
print(nbp // 3)