n = int(input())
while not (1 <= n <= 100):
    n = int(input())

ar = list(map(int,input().split()))

i = 0
ok = True
while (ok == True) and (i < n):
    if ar[i] == 1:
        ok = False
    i += 1

if ok == True:
    print("EASY")
else:
    print("HARD")
