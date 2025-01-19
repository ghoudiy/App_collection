t = int(input())

ar = list(" " * t)
for i in range(t): 
    ar[i] = input()

for i in range(t): 
    ch = ar[i]
    print(ch[::2] + ch[-1])