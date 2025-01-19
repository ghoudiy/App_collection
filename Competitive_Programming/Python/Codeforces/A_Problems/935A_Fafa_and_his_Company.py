def prime(n):
  F = 1
  for i in range(2, int(n ** 0.5)+1):
    if n % i == 0:
      return False
  return True

n = int(input())

S = 1
if prime(n):
  print(S)
else:
  for i in range(2, n // 2 + 1):
    if (n - i) % i == 0:
      S += 1
  print(S)
