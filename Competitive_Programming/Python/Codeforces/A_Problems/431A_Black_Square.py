ar = list(map(int, input().split()))

s = input()
S = 0
for i in range(len(s)): 
    S += ar[int(s[i])-1]

print(S)