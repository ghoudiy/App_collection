n, h = map(int, input().rstrip().split())

a = list(map(int, input().split()))

S = 0
for i in range(n):
    if a[i] > h:
        S += 2
    else:
        S += 1

print(S)
