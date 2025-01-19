from collections import Counter

t = int(input())
for _ in range(t):
  n, q = map(int, input().split())
  a = input()
  b = input()
  for _ in range(q):
    l, r = map(int, input().split())
    aux1 = Counter(sorted(a[l - 1:r]))
    aux2 = Counter(sorted(b[l - 1:r]))
    aux3 = aux1 - aux2
    aux4 = aux2 - aux1
    s = 0
    s2 = 0
    for c1, c2 in zip(aux3.items(), aux4.items()):
      s = 
    print(min(sum((aux1 - aux2).values()), sum((aux2 - aux1).values())))
