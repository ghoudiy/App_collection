n,k = map(int, input().split())

ar = list(map(int ,input().split()))

nbp = 0
for i in range(n): 
    for j in range(i+1,n): 
        if (ar[i] + ar[j]) % k == 0: 
            nbp += 1
print(nbp)

