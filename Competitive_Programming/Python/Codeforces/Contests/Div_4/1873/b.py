from functools import reduce
for _ in range(int(input())):
  n = int(input())
  ar = list(map(int, input().split()))
  m = min(ar)
  ar[ar.index(m)] = m + 1
  print(reduce(lambda x, y: x * y, ar))

