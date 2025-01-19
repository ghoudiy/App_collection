t = int(input()) * 2

arr = []
for _ in range(t): 
    arr.append(list(map(int, input().split())))

for i in range(0,t-1,2): 
    n = arr[i][0]
    i += 1
    ar = arr[i]
    L = []
    maximum = max(ar)
    for i in range(n): 
        if ar[i] != maximum:
            L.append(ar[i])
    if len(L) > 0: 
        nro = maximum - min(L) 
        print(nro)
    else: 
        print(0)
