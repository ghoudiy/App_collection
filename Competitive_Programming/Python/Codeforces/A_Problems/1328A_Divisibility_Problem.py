t = int(input())

ar = []
for i in range(t): 
    ar.append(list(map(int, input().split())))

def divisible(a,b):
    if a % b == 0:
        return 0
    else:
        if b > a:
            return b - a
        else:
            return (b - a % b)
for i in range(t):
    print(divisible(ar[i][0],ar[i][1]))