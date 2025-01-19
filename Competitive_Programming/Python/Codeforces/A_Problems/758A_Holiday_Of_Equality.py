n = int(input())

ar = list(map(int, input().split()))

def maximum(L): 
    maxi = L[0]
    for i in range(1,len(L)): 
        if maxi < L[i]: 
            maxi = L[i]
    return maxi
max = maximum(ar)

S = 0
for i in range(n): 
    S += max - ar[i]

print(S)