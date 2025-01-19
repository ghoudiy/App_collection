n, k, l, c, d, p, nl, np= map(int, input().split())

def minimum(L): 
    min = L[0]
    for i in range(1,len(L)): 
        if min > L[i]: 
            min = L[i]
    return min

litre = k * l
toast = litre // nl
lime = c * d
salt = p // np


nbt = minimum([toast,lime,salt])
print(nbt // n)
