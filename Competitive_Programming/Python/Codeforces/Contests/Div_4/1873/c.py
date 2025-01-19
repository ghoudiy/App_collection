for _ in range(int(input())):
  ar = []
  for _ in range(10):
    ar.append(input())
  s = 0
  for i in range(5):
    aux = 0
    while (p:= ar[i].find("X")) > -1:
      aux = s
      if i <= p <= 10 - i - 1:
        s += i + 1
      else:
        s += abs(p + 1 - 11 * (p // 5))
      ar[i] = ar[i].replace("X", "0", 1)
  for i in range(5):
    while (p:= ar[i + 5].find("X")) > -1:
      aux = s
      if i <= p <= 10 - i - 1:
        s += i + 1
      else:
        s += abs(p + 1 - 11 * (p // 5))
      ar[i + 5] = ar[i + 5].replace("X", "0", 1)
  print(s)
