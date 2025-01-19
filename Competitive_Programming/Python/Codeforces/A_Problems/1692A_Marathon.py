for _ in range(int(input())):
    ar = list(map(int, input().split()))
    a = ar[0]
    nb = 0
    print(sum(1 if x > a else 0 for x in ar))
