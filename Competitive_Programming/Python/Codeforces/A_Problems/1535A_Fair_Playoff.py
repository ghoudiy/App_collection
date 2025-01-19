t = int(input())

arr = []
for _ in range(t):
    arr.append(list(map(int, input().split())))

for _ in range(t):
    ar = arr[_]
    max1 = max(ar[:2])
    max2 = max(ar[2:])
    ar.remove(max1)
    ar.remove(max2)
    if max1 > ar[1] and max2 > ar[0]:
        print("YES")
    else:
        print("NO")
