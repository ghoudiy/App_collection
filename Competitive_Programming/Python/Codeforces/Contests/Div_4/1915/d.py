def main():
  for _ in range(int(input())):
    n = int(input())
    s = input()
    splitted_word = ""
    i = 0
    l = len(s)
    if l > 3:
      nrp = 0
      while i < l - 3:
        if 'bcd'.find(s[i]) != -1 and 'ae'.find(s[i + 1]) != -1:
          nrp += 1
          if 'bcd'.find(s[i + 3]) != -1:
            splitted_word += f"{s[i:i + 3]}."
            i += 3
          else:
            splitted_word += f"{s[i:i + 2]}."
            i += 2
      print(splitted_word + s[len(splitted_word) - l - nrp:])
    else:
      print(s)
main()
