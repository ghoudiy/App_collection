n = int(input())

ch = input()

S = set()
for i in range(n):
    S.add(ch[i].lower())

if len(S) == 26:
    print("YES")
else:
    print("NO")



