n,k = list(map(int, input().split()))

time = 240 - k
ok = True
i = 1
nbm = 0
mm = 0
while (ok == True) and (i <= n):
    mm += 5 * i
    i += 1 
    if mm > time:
        ok = False
    else:
        nbm += 1
print(nbm)

"""
3 222
4 190
7 1
"""