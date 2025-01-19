from random import randint
from pickle import dump, load

def write_file(file_path):
  with open(file_path, 'wb') as file:
    for _ in range(randint(5, 20)):
      dump(randint(-100, 100), file)

def read_file(file_path):
  string = ""
  with open(file_path, 'rb') as file:
    eof = False
    while not eof:
      try:
        x = load(file)
        string += str(x) + " "
      except:
        eof = True
  return string

def count(c, string):
  nrc = 0
  for i in range(len(string)):
    if c == string[i]:
      nrc += 1
  return nrc

def sorting(sorted_path, string: str):
  with open(sorted_path, 'wb') as file:
    for _ in range(count(' ', string)):
      p = string.find(" ")
      minv = int(string[:p])
      a = minv
      aux = string[p+1:]
      p = aux.find(" ")
      while p != -1:
        x = int(aux[:p])
        if minv > x:
          minv = x
        aux = aux[p+1:]
        p = aux.find(" ")

      dump(minv, file)

      p = string.find(" ")
      if a != minv:
        pminv = string.find(f" {minv} ")
        string = string[p+1:pminv] + f" {a} " + string[pminv+len(f" {minv} "):]
        if string[0] == ' ':
          string = string[1:]
      else:
        string = string[p+1:]

def display(sorted_path):
  r = []
  with open(sorted_path, 'rb') as file:
    eof = False
    while not eof:
      try:
        x = load(file)
        print(x)
        r.append(x)
      except:
        eof = True
  print(r == sorted(map(int, string.split(" ")[:-1])))

write_file("Files/numbers.dat")
string = read_file("Files/numbers.dat")
sorting("Files/sorted.dat", string)
display("Files/sorted.dat")
