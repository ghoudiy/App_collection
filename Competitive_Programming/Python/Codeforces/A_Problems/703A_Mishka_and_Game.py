
n = int(input())

m,c = [None] * n, [None] * n

for i in range(n): 
    m[i],c[i] = map(int, input().split())

Sm = 0
Sc = 0
for i in range(n): 
    if m[i] > c[i]: 
        Sm += 1
    elif m[i] < c[i]:
        Sc += 1

if Sm > Sc: 
    print("Mishka")
elif Sm < Sc: 
    print("Chris")
else: 
    print("Friendship is magic!^^")