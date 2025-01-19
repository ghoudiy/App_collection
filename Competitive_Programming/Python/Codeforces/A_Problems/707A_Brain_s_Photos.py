n,m = map(int, input().split())

arr = []
s = ""
for _ in range(n):
    arr.append(list(map(str, input().split())))
    s += "".join(arr[_])

# print("#Color" if [x for x in s if "CMY".find(x) != -1] else "#Black&White")

# Optimization

ok = False
i = 0
while (ok == False) and (i < len(s)):
    ok = "CMY".find(s[i]) != -1
    i += 1
print("#Color" if ok else "#Black&White")
