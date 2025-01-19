ch = input()

L = []
for i in range(len(ch)):
    if ("A" <= ch[i].upper() <= "Z"):
        L.append(ch[i])
print(len(set(L)))