n = int(input())

ar = list(map(int, input().split()))

Ss = 0
Sd = 0
L = []
for i in range(n): 
    m = max(ar[0],ar[-1])
    L.append(m)
    ar.remove(m)
Ss = sum(L[::2])
Sd = sum(L[1::2])
print(Ss,Sd)
