n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

nbg = 0
for i in range(n-1):
    if arr[i] != arr[i+1]:
        nbg += 1

print(nbg+1)

