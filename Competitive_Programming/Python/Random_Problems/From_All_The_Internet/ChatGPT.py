def largest_three_multiply(L):
  N = len(L)
  Max = 0
  for i in range(N - 2):
    for j in range(i + 1, N - 1):
      for k in range(j + 1, N):
        n = L[i] * L[j] * L[k]
        if Max < n:
          Max = n
  return Max


T = sorted(map(int, input().rstrip().lstrip().split()))
for t in range(T.count(0)):
  T.remove(0)
print(largest_three_multiply(T))

# The optimal solution is to find 3 postives max and 2 negatives min
# And return max(max1 * max2 * max3, max1 * min1 * min2)
