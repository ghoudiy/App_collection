for t in range(int(input())):
  a, b = map(int, input().split())
  ans = a - b
  even = ans % 2 == 0
  if (not even and ans < 0) or (even and ans > 0):
    print(1)
  elif (not even and ans > 0) or (even and ans < 0):
    print(2)
  else:
    print(0)
