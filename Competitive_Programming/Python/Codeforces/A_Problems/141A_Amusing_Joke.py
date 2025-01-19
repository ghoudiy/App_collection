S = []

for _ in range(3): 
    S.append(input())

def Freq(c,ch):
    F = 0
    for i in range(len(ch)):
        if c == ch[i]:
            F += 1
    return F 

def Tri_Bulle(ch):
    ok = True 
    while ok == True:
        ok = False
        i = 0
        while (ok == False) and (i < len(ch) - 1): 
            if ch[i] > ch[i + 1]:
                aux = ch[i]
                ch[i] = ch[i+1]
                ch[i+1] = aux
                ok = True
            i += 1
    return ch

ch1 = list(S[0] + S[1])
ch2 = list(S[2])
# To avoid build_in_function and to practice Tri 
ch1 = Tri_Bulle(ch1)
ch2 = Tri_Bulle(ch2)
# ch1.sort()
# ch2.sort()
if len(ch1) == len(ch2):
    ok = True
    i = 0
    while (ok == True) and (i < len(ch1)): 
        F1 = Freq(ch1[i],ch1)
        F2 = Freq(ch2[i],ch2)
        if F1 != F2:
            ok = False
        i += 1
    if ok == True:
        print("YES")
    else: 
        print("NO")
else: 
    print("NO")

