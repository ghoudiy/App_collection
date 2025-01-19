def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        ar = list(map(int, input()))
        s = sum(ar) / n
        for i in range(n - 1):
            if abs(ar[i] - ar[i + 1]) > k:
                ar.remove(ar[i])
        

main()

