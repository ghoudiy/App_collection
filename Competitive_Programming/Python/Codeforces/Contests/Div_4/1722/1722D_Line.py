# Working
def Sum_all(s):
  S = 0
  for i in range(n):
    if s[i] == 'L':
      S += len(s[:i])
    else:
      S += len(s[i+1:])
  return S

def Maximum(s, k, n, ans):
  i = 0
  j = 0
  tmp = s
  while j < k and i < n:
    while i < n - 1 and s[i] == "R" and s[n-i-1] == "L":
      i += 1
    if s[i] == "L" and i < n // 2:
      s = s[:i] + "R" + s[i+1:]
      ans += len(s[i+1:]) - len(s[:i])
    elif s[n-i-1] == "R" and i < n // 2:
      s = s[:n-i-1] + "L" + s[n-i:]
      ans += len(s[:n-i-1]) - len(s[n-i:])
    j += 1
  tmp = "R" * (n // 2) + "L" * (n // 2)
  tmp += "L" if n % 2 != 0 else ""
  if s == tmp:
    return [ans, 1]
  return [ans, 0]


for t in range(int(input())):
  n = int(input())
  s = input()
  Max = [0, 0]
  S = Sum_all(s)
  for i in range(len(s)):
    if Max[1] > 0:
      print(Max[0], end=" ")
    else:
      res = Maximum(s, i+1, n, S)
      if Max[0] == res[0] or res[1] > 0:
        Max[1] = 1
      else:
        Max[1] = 0
      Max[0] = res[0]
      print(res[0], end=" ")
  print()
