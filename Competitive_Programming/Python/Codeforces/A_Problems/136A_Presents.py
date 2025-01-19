n = int(input())
while not (1 <= n <= 100):
    n = int(input())

ar = list(map(int, input().split()))

L = [0] * n
for i in range(n):
    L[ar[i]-1] = i + 1 
for l in L:
    print(l,end=" ")
