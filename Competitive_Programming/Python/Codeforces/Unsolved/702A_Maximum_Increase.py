def main():
    n = int(input())
    ar = list(map(int, input().split()))
    i = t = 0
    for i in range(n - 1):
        t += 1 if ar[i] < ar[i + 1] else 0
    print(t)

main()
