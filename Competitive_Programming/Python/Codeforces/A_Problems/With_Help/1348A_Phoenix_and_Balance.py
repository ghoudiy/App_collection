for _ in range(int(input())):
  n = int(input())
  x=0
  y=0
  for i in range(1,(n//2)):
    x = x+2**i
  a=(2**n)+x
  for j in range(1,n+1):
    y=y+2**j
  b=y-a
  # print(a)
  # print(b)
  print(abs(a-b))

