def main():
  for _ in range(int(input())):
    n = int(input())
    maxq = 1
    maxi = 1
    for i in range(n):
      a, b = map(int, input().split())
      if a <= 10 and maxq < b:
        maxq = b
        maxi = i + 1
    print(maxi)


main()

