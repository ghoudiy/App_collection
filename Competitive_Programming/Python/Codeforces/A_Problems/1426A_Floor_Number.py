for _ in range(int(input())):
  n, x = map(int, input().split())
  ok = 1 <= n <= 2
  nrf = 1 if ok else 2
  lb = 3
  ub = x + 2
  i = 1
  while not ok:
    ok = lb <= n <= ub
    if not ok:
      lb = i * x + 3
      ub = (i + 1) * x + 2
      nrf += 1
      i += 1
  print(nrf)

# Or (I will think of it)
# from math import ceil
# for _ in range(int(input())):
  # n, x = map(int, input().split())
  # print(n / x)
