for _ in range(int(input())): 
  n = int(input())
  arc = list(map(int, input().split()))
  aro = list(map(int, input().split()))
  min_arc = min(arc)
  min_aro = min(aro)
  nrm = 0
  for i in range(n):
    nrm += max(arc[i] - min_arc, aro[i] - min_aro)
  print(nrm)
