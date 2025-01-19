ar = [int(input()) for i in range(5)]
S = 0
for i in range(1, ar[4] + 1):
  if i % ar[0] != 0 and i % ar[1] != 0 and i % ar[2] != 0 and i % ar[3] != 0:
    S += 1
print(ar[4] - S)
# Simply
