t = int(input())

ar = list("0" * t)
for i in range(t): 
    ar[i] = int(input())


for i in range(t): 
    num = ar[i]
    L = []
    d = 1
    while num > 0:
        u = (num % 10) * d
        d *= 10
        num //= 10
        if u > 0: 
            L.append(u)
    print(len(L))
    print(" ".join(map(str, L)))
        
# for _ in range(int(input())):
#     n=int(input())
#     p=1
#     rl=[]
#     x=[]
#     while(n>0):
#         dig=n%10
#         r=dig*p
#         rl.append(r)
#         p*=10
#         n=n//10
#     for i in rl:
#         if i !=0:
#             x.append(i)
#     print(len(x))
#     print(" ".join(str(x)for x in x))
