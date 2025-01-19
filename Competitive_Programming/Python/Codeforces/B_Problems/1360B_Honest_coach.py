t = int(input()) * 2

arr = []
for _ in range(t): 
    arr.append(list(map(int, input().split())))

for i in range(0,t-1,2):
    n = arr[i][0]
    i += 1
    ar = sorted(arr[i])
    L = []
    for i in range(len(ar)-1): 
        L.append(ar[i+1] - ar[i])
    print(sorted(L)[0])
