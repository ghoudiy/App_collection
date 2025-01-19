def main():
  for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print("YES" if b + c >= 10 else "NO")

main()

