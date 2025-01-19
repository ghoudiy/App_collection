for _ in range(int(input())):
    s = input()
    S1 = sum([int(x) for x in s[:3]])
    S2 = sum([int(x) for x in s[3:]])
    print("YES" if S1 == S2 else "NO")
