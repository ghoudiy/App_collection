n, m = map(int, input().split())
t = -1
for i in range(1, n, 2):
	print("#" * m)
	s = ["."] * (m + 1)
	s[t] = "#"
	t *= -1
	print("".join(s[1:]))
print("#" * m)
