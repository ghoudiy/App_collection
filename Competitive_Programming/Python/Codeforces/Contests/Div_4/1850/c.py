def main():
    for _ in range(int(input())):
        ans = ""
        for i in range(8):
            ans += input().replace(".", "")
        print(ans)

main()

