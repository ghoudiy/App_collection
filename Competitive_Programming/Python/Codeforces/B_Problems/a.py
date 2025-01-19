import codeforces_oop
codeforces_oop.problem("1535B").run_demo()

t = int(input())

arr = []
for _ in range(t):
    arr.append(int(input())) 
    arr.append(list(map(int, input().split())))

for i in range(0,t*2,2): 
    n, ar = arr[i] ,arr[i + 1]
    a = ar[:]
    b = ar[:]
    for _ in range(n): 
        maxv = max(b)
        minv = min(a)
        if minv < maxv: 
            l = b.index(maxv)
            j = a.index(minv)
            Aux = b[l]
            b[l] = a[j]
            a[j] = Aux
    print(sum(a))

