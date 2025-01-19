from numpy import array

def initialize_ar(T, M, dc, ph):
  for i in range(len(ph)):
    T[i] = dict()
    T[i]["distance"] = M[ord(dc) - 65, ord(ph[i]) - 65]
    T[i]["path"] = dc
    T[i]["node"] = ph[i]


def min_distance(T, ph, aux):
  minv = T[aux.find(ph[0])]["distance"]
  mini = 0
  for i in range(1, len(ph)):
    p = aux.find(ph[i])
    if T[p]["distance"] < minv:
      minv = T[p]["distance"]
      mini = i
  return mini

def min_path(ph: str, M, dc, ca):
  p = ph.find(dc)
  ph = ph[:p] + ph[p+1:]
  T = array([dict()] * len(ph), dtype=dict)
  initialize_ar(T, M, dc, ph)
  aux = ph
  min_indice = min_distance(T, ph, aux)
  min_char = ph[min_indice]
  p = min_indice
  while min_char != ca:
    distance = T[p]["distance"]
    path = T[p]["path"]
    ph = ph[:min_indice] + ph[min_indice+1:]

    for i in range(len(ph)):
      x = M[ord(min_char) - 65, ord(ph[i]) - 65] + distance
      p = aux.find(ph[i])
      if x < T[p]["distance"]:
        T[p]["distance"] = x
        T[p]["path"] = path + min_char
    min_indice = min_distance(T, ph, aux)
    min_char = ph[min_indice]
    p = aux.find(min_char)

  e = dict()
  p = aux.find(ca)
  e["path"] = T[p]["path"] + ca
  e["distance"] = T[p]["distance"]
  return e

def initialize(M, distance_file_path, ph):
  with open(distance_file_path, 'r') as distance_file:
    lines = distance_file.readlines()
    for line in lines[:-2]:
      line = line.replace(" ", "")
      ph.add(line[1])
      ph.add(line[3])
      M[ord(line[1]) - 65, ord(line[3]) - 65] = int(line[6:len(line) - 1])
      M[ord(line[3]) - 65, ord(line[1]) - 65] = int(line[6:len(line) - 1])
  return lines[-2][:-1], lines[-1]
ph = set()
from math import inf
M = array([[100000] * 10] * 10, dtype=int)
dc, ca = initialize(M, "/home/ghoudiy/Public/input_files/input.txt", ph)
e = min_path("".join(ph), M, dc, ca)
a = e["path"]
L = []
for i in range(len(a)-1):
  L.append(M[ord(a[i]) - 65, ord(a[i+1]) - 65])
