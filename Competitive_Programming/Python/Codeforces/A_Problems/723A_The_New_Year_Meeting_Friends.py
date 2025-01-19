def Tri_Bulle(L): 
    ok = True
    while ok == True:
        ok = False
        for i in range(len(L) - 1): 
            if L[i] > L[i+1]: 
                Aux = L[i+1]
                L[i+1] = L[i]
                L[i] = Aux
                ok = True
    return L

x1,x2,x3 = Tri_Bulle(list(map(int, input().split())))

def diff(a,b): 
    while a != b: 
        if a > b: 
            return b - a
        else: 
            return a - b

print(abs(diff(x1,x2) + diff(x3,x2)))