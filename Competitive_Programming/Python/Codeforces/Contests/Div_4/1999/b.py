def score(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    return 0

def main():
    for _ in range(int(input())):
        a1, a2, b1, b2 = map(int, input().split())
        s = 0
        if score(a1, b1) + score(a2, b2) > 0:
            s += 2
        if score(a1, b2) + score(a2, b1) > 0:
            s += 2
        print(s)
main()

