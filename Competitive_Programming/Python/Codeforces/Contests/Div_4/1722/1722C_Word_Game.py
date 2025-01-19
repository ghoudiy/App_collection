def score(S1, S2, S3, R, T):
  it2 = S1.intersection(S2)
  it3 = S1.intersection(S3)
  it2, it3 = it2.difference(it3), it3.difference(it2)
  S1.difference_update(it2 | it3)
  S2.difference_update(it2)   
  S3.difference_update(it3)   
  it2 = len(it2)
  it3 = len(it3)
  R[T[0]] += it2 + it3 + len(S1.difference(S2 | S3)) * 3
  R[T[1]] += it2
  R[T[2]] += it3
  
for t in range(int(input())):
  n = int(input())
  s1 = set(input().split())
  s2 = set(input().split())
  s3 = set(input().split())
  R = [0, 0, 0]
  score(s1, s2, s3, R, [0, 1, 2])
  score(s2, s1, s3, R, [1, 0, 2])
  score(s3, s1, s2, R, [2, 0, 1])
  print(*R)
