for _ in range(int(input())):
	a, b, c, n = map(int, input().split())
	a, b, c = sorted([a, b, c])
	ans = n - (2 * c - b - a)
	print("YES" if ans >= 0 and ans % 3 == 0 else "NO")
