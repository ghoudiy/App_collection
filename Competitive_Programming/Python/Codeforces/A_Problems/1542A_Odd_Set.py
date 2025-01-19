for _ in range(int(input())):
  n = int(input())
  ar = list(map(int, input().split()))
  even = 0
  odd = 0
  for num in ar:
    if num % 2 == 0:
      even += 1
    else:
      odd += 1
  print("Yes" if even == odd else "No")
