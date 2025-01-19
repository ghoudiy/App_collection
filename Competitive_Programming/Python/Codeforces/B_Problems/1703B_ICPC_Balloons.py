for _ in range(int(input())):
  n = int(input())
  s = input()
  l = len(set(s))
  print(l * 2 + (len(s) - l))
