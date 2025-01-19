def main():
  t = int(input())
  for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    nre = 0
    nro = 0
    for num in a:
      if num % 2 == 0:
        nre += 1
      else:
        nro += 1
    for _ in range(q):
      nr1 = nre
      nr2 = nro
      l, r, k = map(int, input().split())
      for i in range(l - 1, r):
        if a[i] % 2 == 0:
          nr1 -= 1
        else:
          nr2 -= 1
      if k % 2 == 0:
        nr1 += r - l + 1
      else:
        nr2 += r - l + 1
      nr2 %= 2
      print("NO" if nr1 == 0 and n % 2 == 0 or nr2 == 0 else "YES")

main()
