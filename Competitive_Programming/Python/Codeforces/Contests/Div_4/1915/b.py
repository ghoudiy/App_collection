from collections import Counter
def main():
  s = Counter("AAABBBCCC")
  for _ in range(int(input())):
    c = ""
    for _ in range(3):
      c += input()
    print(next((s - Counter(c)).elements()))

    

main()

