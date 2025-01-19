for _ in range(int(input())):
  n, s, m = map(int, input().split())
  last_task = 0
  msg = "NO"
  for _ in range(n):
    l, r = map(int, input().split())
    if l - last_task >= s:
      msg = "YES"
    last_task = r
  if msg != "YES" and m - last_task >= s:
    msg = "YES"
  print(msg)
    