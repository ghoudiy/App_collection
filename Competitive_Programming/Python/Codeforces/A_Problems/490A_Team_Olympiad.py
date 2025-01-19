n = int(input())

t = list(map(int, input().split()))

def minimum(L): 
    minn = L[0]
    for i in range(1,len(L)): 
        if minn > L[i]: 
            minn = L[i]
    return minn
    
def Freq(c,ch): 
    F = 0
    for i in range(len(ch)):
        if c == ch[i]: 
            F += 1
    return F 

F1 = Freq(1,t)
F2 = Freq(2,t)
F3 = Freq(3,t)
    
min = minimum([F1,F2,F3])

print(min)
for i in range(min): 
    i1 = t.index(1)
    i2 = t.index(2)
    i3 = t.index(3)
    print(i1+1,i2+1,i3+1)
    t[i1] = 0
    t[i2] = 0
    t[i3] = 0
    


# What is all of this



# arr = []
# i = -1
# while F1 > 0 and F2 > 0 and F3 > 0 and i < n:
#     i += 1
#     S = {t[i]}
#     if t[i] == 0: 
#         continue
#     L = [i+1]
#     S.discard(0)
#     j = i+1
#     while len(S) < 3: 
#         nb = len(S)
#         S.add(t[j])
#         S.discard(0)
#         nb1 = len(S)
#         if nb1 > nb: 
#             L.append(j+1)
#             t[j] = 0
#         j += 1

#     F1 -= 1
#     F2 -= 1
#     F3 -= 1
#     arr.append(L)

# print(len(arr))
# for i in range(len(arr)): 
#     print(" ".join(map(str,arr[i])))