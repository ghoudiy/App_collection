t = int(input()) * 2

arr = []
for i in range(t):
    arr.append(list(map(int, input().split())))

for i in range(0,t-1,2):
    n = arr[i][0]
    i += 1
    ar = arr[i]
    for j in range(n): 
        F = ar.count(ar[j])
        if F == 1: 
            print(j+1)
