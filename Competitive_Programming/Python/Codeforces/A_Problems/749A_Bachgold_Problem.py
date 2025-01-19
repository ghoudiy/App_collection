n = int(input())
ch = ("2 " * (n // 2))[:-1] if n % 2 == 0 else "2 " * (n // 2 - 1) + "3"
print(len(ch.split(" ")), ch, sep="\n")
