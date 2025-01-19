def saisie(bi,bs):
    ch = input().strip()
    while not (bi <= len(ch) <= bs):
        ch = input().strip()
    return ch

s = saisie(1,100)
t = saisie(1,100)
R = ''

for i in range(len(s)):
     R += s[len(s)-i-1]

if R == t:
    print("YES")
else:
    print("NO")
