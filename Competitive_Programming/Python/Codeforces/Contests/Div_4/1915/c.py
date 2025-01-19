def main():
  for _ in range(int(input())):
    n = int(input())
    ar = map(int, input().split())
    s = sum(ar)
    if (s ** 0.5) == int(s ** 0.5):
      print("YES")
    else:
      print("NO")    
    

main()

