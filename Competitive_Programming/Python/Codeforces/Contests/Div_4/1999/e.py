def divide(n, m):
  nb = 0
  while n > 0:
    nb += 1
    m *= 3
    n = round(n / 3)
  return nb, m

for _ in range(int(input())):
  l, r = map(int, input().split())
  if (l + 1) // 3 == 0:
    nb, m = divide(l + 1, l)
  else:
    nb, m = divide(l, l + 1)
  print(f"{nb = }")
  print(f"{m = }")
  print(nb + m // 3 + 1 + sum(i // 3 + 1 for i in range(l + 2, r + 1)))
