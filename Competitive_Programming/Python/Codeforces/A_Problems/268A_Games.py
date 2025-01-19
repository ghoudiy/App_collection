n = int(input())

h = []
a = []

for i in range(n): 
    ar = list(map(int,input().split()))
    h.append(ar[0])
    a.append(ar[1])

nbg = 0

for i in range(n): 
    for j in range(n):
        if h[i] == a[j] and i != j: 
            nbg += 1 


print(nbg)