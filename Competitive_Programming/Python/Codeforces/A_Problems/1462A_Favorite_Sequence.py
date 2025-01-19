for _ in range(int(input())):
  n = int(input())
  ar = list(map(int, input().split()))
  L = []
  x = 0
  for i in range(n):
    if i % 2 == 0:
      L.append(ar[x])
      x += 1
    else:
      L.append(ar[n - x])
  print(*L)
