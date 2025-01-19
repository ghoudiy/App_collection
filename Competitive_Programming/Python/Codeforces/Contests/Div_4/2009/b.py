for _ in range(int(input())):
  n = int(input())
  s = ""
  for _ in range(n):
    s = f" {input().find('#') + 1}" + s
  print(s[1:])