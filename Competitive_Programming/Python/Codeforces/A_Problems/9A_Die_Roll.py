from math import gcd
y, w = sorted(map(int, input().split()))
L = set(range(w, 7))
L.add(y + w) if y + w <= 6 else None
d = gcd(len(L), 6)
match t:= len(L):
  case 6 : print("1/1")
  case 0 : print("0/1")
  case _: print(f"{t // d}/{6 // d}")
