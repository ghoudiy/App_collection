for _ in range(int(input())):
  a, b = map(int, input().split())
  c = (a + b) // 2
  print((c - a) + (b - c))