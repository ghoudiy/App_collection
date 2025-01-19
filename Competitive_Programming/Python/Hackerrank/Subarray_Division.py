n = int(input())

s = list(map(int, input().rstrip().split()))

d,m = map(int, input().split())


nbw = 0
for i in range(n-m+1):
    S = 0
    for j in range(m): 
        S += s[i+j]
    if S == d: 
        nbw += 1
print(nbw)