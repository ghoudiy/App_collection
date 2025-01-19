y = int(input())
while not (1000 <= y <= 9000):
    y = int(input())

def freq(c,ch):
    F = 0
    for i in range(len(ch)):
        if c == ch[i]:
            F += 1
    return F

ok = False

while ok == False:
    ok = True
    y += 1
    ch = str(y)
    tmp = True
    i = 0
    while (tmp == True) and (i != 4):
        F = freq(ch[i],ch)
        if F > 1:
            tmp = False
            ok = False
        i += 1
print(y)
