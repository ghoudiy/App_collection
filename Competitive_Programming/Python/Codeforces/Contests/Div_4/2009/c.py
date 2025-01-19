for _ in range(int(input())):
  x, y, k = map(int, input().split())
  xf = x // k
  yf = y // k
  print(max(xf, yf) * 2 + (2 if xf * k < x or yf * k < y else 0))