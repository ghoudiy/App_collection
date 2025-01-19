n = int(input())

ar = list(map(int, input().split()))

def minimum(T):
    minii = T[0]
    for i in range(1,n):
        if minii >= T[i]:
            minii = T[i]
            x = i

    return minii,x
    
maxv = max(ar)
ok = True 
i = ar.index(maxv)
nbs = 0
while ok:
    ok = False
    if maxv != ar[0] and i > 0:
        Aux = ar[i-1]
        ar[i-1] = ar[i]
        ar[i] = Aux
        i -= 1
        nbs += 1
        ok = True

mini,j = minimum(ar)
ok = True
while ok:
    ok = False
    if mini != ar[-1] and j < n - 1:
        Aux = ar[j+1]
        ar[j+1] = ar[j]
        ar[j] = Aux
        j += 1
        nbs += 1
        ok = True

print(nbs)
