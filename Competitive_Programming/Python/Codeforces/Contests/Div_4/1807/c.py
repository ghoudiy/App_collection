def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    letter_index_dict = {}
    test = True
    i = 0
    while test and i < n:
      if letter_index_dict.get(s[i]) is None:
        letter_index_dict[s[i]] = i
      else:
        if (i - letter_index_dict[s[i]]) % 2 != 0:
          test = False
        letter_index_dict[s[i]] = i
      i += 1
    print("YES" if test else "NO")
      
main()
