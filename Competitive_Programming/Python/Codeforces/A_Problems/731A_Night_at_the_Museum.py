s = input()
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nrm = 0
for letter in s:
  p = abc.index(letter)
  abc = abc[p:] + abc[:p]
  nrm += min(p, abs(p - 26))
print(nrm)
