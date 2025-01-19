n = int(input())

L = [100, 20, 10, 5, 1]

nbg = 0
while n > 0: 
    for num in L:
        if n >= num: 
            nbg += (n // num)
            n %= num 
    
print(nbg)