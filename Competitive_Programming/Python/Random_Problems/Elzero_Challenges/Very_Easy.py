# Find English Letter Position
def find_position_for(letter):
  def Method_1(letter):
    return ord(letter.upper()) - 64
  def Method_2(letter):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.find(letter) + 1
  return Method_1(letter)
  return Method_2(letter)
# Testing Ouput
print(find_position_for("C")) # 3
print(find_position_for("P")) # 16

# Find Missing letter in Sequence

def find_missing_letter_in(letters):
  i = -1
  ok = True
  while ok and i < len(letters) - 1:
    i += 1
    ok = ord(letters[i]) == ord(letters[0]) + i
  if ok:
    return "No Missing Letter in Sequence"
  else:
    return chr(ord(letters[0]) + i)

# Testing Ouput
print(find_missing_letter_in("abcdeghi")) # f
print(find_missing_letter_in("defgi")) # h
print(find_missing_letter_in("xyz")) # No Missing Letter In Sequence

# Swap Cases And Remove Numbers
def swapping(word):
  i = 0
  while i < len(word):
    if not word[i].isalpha():
      word = word[:i] + word[i+1:]
      i -= 1
    elif word[i] == word[i].upper():
      word = word[:i] + word[i].lower() + word[i+1:]
    elif word[i] == word[i].lower():
      word = word[:i] + word[i].upper() + word[i+1:]
    i += 1
  return word

# Test Cases
print(swapping("HellO"))  # hELLo
print(swapping("WOrld"))  # woRLD
print(swapping("12ProGRAM12"))  # pROgram

# Number To Reversed List
def convert(n):
  return list(map(int, list(str(n))[::-1]))

# Testing Ouput
print(convert(564987654))  # [4, 5, 6, 7, 8, 9, 4, 6, 5]
print(convert(529132)) # [2, 3, 1, 9, 2, 5]

# Remove Duplicate Words

def remove_duplicate_words_from(sentence):
  def Method_1(sentence):
    i = 0
    L = sentence.split()
    while len(L) != len(set(L)):
      e = sentence[i:].find(" ")
      word = sentence[i:e+i]
      p = sentence[e+i+1:].find(word)
      if p > -1:
        sentence = sentence[:e+p+i] + sentence[e+i+p+len(word)+1:]
      i = e + 1 + i
      L = sentence.split()
    return sentence
  def Method_2(sentence) -> str:
    L = sentence.split()
    s = L[0] + " "
    for word in L[1:]:
      p = s.find(word)
      print(word, p)
      if p == -1 or (p > -1 and s[p-1] != " " and s[p+len(word)] != " "):
        s += f"{word} "
        print(s)
    return s[:-1]
  return Method_2(sentence)
# Testing Ouput
print(remove_duplicate_words_from("Hello Elzero Web Web Hello School"))
# Hello Elzero Web School