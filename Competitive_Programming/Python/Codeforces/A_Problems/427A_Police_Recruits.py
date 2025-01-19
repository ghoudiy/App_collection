n = int(input())

ar = list(map(int, input().split()))

nbc = 0
nbp = 0
for i in range(n): 
    if ar[i] > -1:
        nbp += ar[i]
    elif ar[i] == -1 and nbp == 0:
        nbc += 1
    elif ar[i] == -1 and nbp > 0:
        nbp -= 1

print(nbc)