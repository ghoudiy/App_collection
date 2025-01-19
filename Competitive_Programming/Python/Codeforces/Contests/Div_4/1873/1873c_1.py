for _ in range(int(input())):
  ar = []
  for _ in range(10):
    ar.append(input())
  s = 0
  for i in range(5):
    # print("-" * 20)
    # print(f"{i = }")
    for j in range(i, 10 - i):
      if i != j:
        # print((i, j), (j, i), (10-i-1, j), (j, 10-i-1))
        # print(ar[i][j],
        #   ar[j][i],
        #   ar[10-i-1][j],
        #   ar[j][10-i-1]
        # )
        s += (i + 1) * (ord(ar[i][j]) // 88)
        s += (i + 1) * (ord(ar[j][i]) // 88)
      if 10 - i - 1 != j:
          
        s += (i + 1) * (ord(ar[10-i-1][j]) // 88)
        s += (i + 1) * (ord(ar[j][10-i-1]) // 88)
  # print(ar[-1], "ar[-1]")
  print(s)
