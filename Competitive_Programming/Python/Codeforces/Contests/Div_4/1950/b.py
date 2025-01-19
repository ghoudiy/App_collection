for _ in range(int(input())):
  n = int(input())
  s = ""
  s2 = ""
  for i in range(0, 2 * n, 2):
    s += ".#"[i % 4 == 0] * 2
    s2 += ".#"[i % 4 != 0] * 2
  s += "\n" + s
  s2 += "\n" + s2
  ans = ""
  for i in range(n):
    ans += [s, s2][i % 2] + "\n"
  print(ans, end="")
    