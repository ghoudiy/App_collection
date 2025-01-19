def main():
  t = int(input())
  for _ in range(t):
    _ = int(input())
    a = map(int, input().split())
    nb = 0
    nb2 = 0
    for num in a:
      if num % 2 == 0:
        nb += num
      else:
        nb2 += num
    print("YES" if nb > nb2 else "NO")

main()

