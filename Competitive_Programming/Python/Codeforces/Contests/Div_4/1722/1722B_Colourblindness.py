for _ in range(int(input())):
  n = int(input())
  s1 = input()
  s2 = input()
  i = 0
  ok = True
  while ok and i < n:
    if s1[i] == "R" or s2[i] == "R":
      ok = s1[i] == "R" and s2[i] == "R"
    i += 1
  print("YES" if ok else "NO")
