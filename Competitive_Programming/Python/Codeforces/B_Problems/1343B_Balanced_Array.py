t = int(input())

ar = []
for i in range(t): 
    ar.append(int(input()))

for i in range(t): 
    ar1 = []
    n = ar[i]
    num = 0
    Se = 0
    for j in range(n//2):
        num += 2 
        ar1.append(num)
        Se += num
    So = 0
    num = 1
    n //= 2
    while n > 1 : 
        So += num
        ar1.append(num)
        num += 2
        n -= 1
    while So < Se: 
        num += 2
        if So + num >= Se: 
            So += num
    if So == Se: 
        print("YES")
        ar1.append(num)
        print(" ".join(map(str, ar1)))
    else:
        print("NO")

