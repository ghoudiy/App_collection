a,b = list(map(int, input().split()))

nbd = 0
nbs = 0
while (a > 0 or b > 1) and (a > 1 or b > 0):
    if a >= 1 and b >= 1:
        nbd += 1
        a -= 1
        b -= 1
    elif a >= 2:
        nbs += 1
        a -= 2
    elif b >= 2:
        nbs += 1
        b -= 2

print(nbd,nbs) 