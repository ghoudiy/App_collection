m = [[0] * 10 for i in range(10)]
for i in range(5):
  for j in range(i, 10 - i):
    m[i][j] = (i + 1)
    m[j][j] = (i + 1)
    m[10-i-1][j] = (i + 1)
    m[j][10-i-1] = (i + 1)
  for j in range(i):
    m[i][j] = j + 1
    m[10-i-1][j] = j + 1

for _ in range(int(input())):
  ar = []
  for i in range(10):
    ar.append(input())
  s = 0
  for i in range(10):
    for j in range(10):
      s += m[i][j] * (ord(ar[i][j]) // 88)
  print(s)
