n = int(input())
while not (1 <= n <= 100,000):
    n = int(input())

ch = input()

nba = 0
nbd = 0
for i in range(n):
    if ch[i] == "A":
        nba += 1
    else:
        nbd += 1

if nba > nbd:
    print("Anton")
elif nbd > nba:
    print("Danik")
else:
    print("Friendship")
