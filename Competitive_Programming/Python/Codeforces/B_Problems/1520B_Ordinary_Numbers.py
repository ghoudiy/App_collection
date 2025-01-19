for _ in range(int(input())):
  n = int(input())
  l = len(str(n))
  nro = l * 9
  x = str(10 ** l - 1 - n)
  nro -= int(x[0]) if len(x) >= l else 0
  nro -= (n < int(str(n)[0] * l))
  print(nro)
