for _ in range(int(input())):
  s = list(input())
  t = input()
  i = 0
  j = 0
  l = len(t)
  l1 = len(s)
  while j < l and i < l1:
    if s[i] == '?':
      s[i] = t[j]
      j += 1
    elif s[i] == t[j]:
      j += 1
    i += 1
  if j == l:
    print(f"YES\n{''.join(s).replace('?', 'a')}")
  else:
    print("NO")
