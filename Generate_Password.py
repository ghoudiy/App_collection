from sys import argv
from random import shuffle, randint


def Password(long):
  num = str(randint(0, 9999)).zfill(4)
  nums = list(range(0,10))
  sym = list(filter(lambda ch: not ch.isalnum(), map(lambda x: chr(x), range(33,127))))
  sym = [x for x in sym if (x not in ["'", '"'])]
  letters = list(map(chr, range(65,91)))
  letters = list(map(lambda ch: ch.lower(), letters)) + letters
  L = nums + sym + letters
  shuffle(L)
  L.insert(randint(0,long-5),num) if long >= 10 else 0
  s = "".join(map(str, L))[:long]
  while len(s) < long:
    s += Password(long)[:long-len(s)]
  return s


if __name__ == "__main__":
  print("Press enter for a random length between 8 and 20")
  long = input("Password length: ")
  if long == "":
    long = randint(8, 20)
  else:
    long = int(long)
  print(f"A Random Password of Length {long}= \"{Password(long)}\" (without quotes)")

def cli():
  if argv[1].isdigit():
    print(f"A Random Password of Length {argv[1]}= \"{Password(int(argv[1]))}\" (without quotes)")
