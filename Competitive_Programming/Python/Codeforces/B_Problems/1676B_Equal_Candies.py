t = int(input())
for _ in range(t):
  n = int(input())
  ar = list(map(int, input().split()))
  y = min(ar)
  print(sum(x - y for x in ar)) 
