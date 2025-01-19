from sys import platform
import os 
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def type_file(p):
  if os.path.isfile(p):
    t = "file"
  elif os.path.islink(p):
    t = "link"
  elif os.path.isdir(p):
    t = "dir"
  return t


def Ident(s1, s2):
  i = -1
  ok = True
  while ok and i < len(s1) - 1:
    i += 1
    ok = s1[i] == s2[i]
    if not ok:
      j = 0
      test = True
      while test and j < len(s1[i]):
        test = s1[i][j] == s2[i][j]
        j += 1
  if ok:
    return -1
  return i, j 


def Diff(path_1, path_2, t1, t2, c=""):
  type_1 = t1 == "link" and t2 == "link"
  type_2 = t1 == "link" and t2 == "file"
  type_3 = t1 == "file" and t2 == "link"
  if type_1 or type_2 or type_3: # Link
    test = os.path.samefile(path_1, path_2)
    if test and type_1:
      return "The two links reference the same actual file!"
    elif test and (type_2 or type_3):
      return "The two paths reference the same actual file!"
    else:
      return "The two paths not reference the same actual file!"
  
  elif t1 == "dir": # Directory

    # Extracting the different and similar files by their names
    content_1 = set(content(path_1, t1))
    content_2 = set(content(path_2, t2))
    if platform == "Windows":
      content_1 = {x.lower() for x in content_1}
      content_2 = {x.lower() for x in content_2}
      path_1 += "\\" if path_1[-1] != "\\" else ""
      path_2 += "\\" if path_2[-1] != "\\" else ""
    else:
      path_1 += "/" if path_1[-1] != "/" else ""
      path_2 += "/" if path_2[-1] != "/" else ""

    Differ = content_1.symmetric_difference(content_2)
    Similar = content_1.intersection(content_2)

    Fo = []
    Fi = []
    for element in Similar:
      if os.path.isdir(path_1 + element):
        Fo.append(element)
      
      elif os.path.isfile(path_1 + element):
        Fi.append(element)

    Res = dict()

    if len(Fo) > 0:
      if c == "":
        c = input("Search the difference in subfolders? [Y/n]").lower()
        while c != "n" and c != "y" and c != "":
          c = input("[Y/n] ").lower()

      if c == '' or c == 'y':
        D = []
        for folder in Fo:
          D.append(Diff(f"{path_1 + folder}", f"{path_2 + folder}", "dir", "dir", 'y'))
        
        if len(D) > 0:
          Res["dir"] = D
          print("SUBDIRECTORY: ", D)
          print(Res)
    print("FILES: ", Fi, f"{path_1 = }, {path_2 = }")
    if len(Fi) > 0:
      F = []
      for file in Fi:
        s1 = open(f"{path_1 + file}", 'r').readlines()
        s2 = open(f"{path_2 + file}", 'r').readlines()
        r = Ident(s1, s2)
        if type(r) == tuple:
          # F.append(f"Path 1: {file}   Path 2: {file}  differ: line {r[0]}, byte {r[1]}")
          F.append(f"{path_1 + file}  and  {path_2 + file}  differ: line {r[0]}, byte {r[1]}")

      if len(F) > 0:
        Res["file"] = F
    
    if len(Differ) > 0:
      Res["diff"] = Differ

    if (len(Fi) > 0 and len(F) == 0 or len(Fi) == 0) and (len(Fo) > 0 and len(D) > 0 or len(Fo) == 0) and len(Differ) == 0:
      return f"The two directorys {path_1} and {path_2} have the same files!"
    
    return Res

  else: # File
    r = Ident(open(path_1, 'r').read(), open(path_2, 'r').read())
    if len(r) > 1:
      return (f"{path_1 + file}  and  {path_2 + file}: line {r[0]}, byte {r[1]}")
    return "The two files are the same!"


def Intersection(path_1, path_2, content_1, content_2):
  Simil = set(content_1).intersection(set(content_2))


# Assign the value of the path according to its type
def content(p, t):
  if t == "dir":
    return os.listdir(p)
  return open(p, 'r').read()


def CLI():
  # Entering paths
  def Entering(s, p1='', t=''):
    p = input(f"The {s} path: ")
    while not os.path.exists(p):
      p = input(f"The Given path is invalid. Please check your path and try again!\nThe {s} path: ")
    while p == p1 and p1 != '':
      p = input("You entered the same path\nPlease enter new one: ")
    while t != type_file(p) and t != '':
      p = input(f"TypeError: unsupported operand types for difference: '{t}' and '{type_file(p)}'")
    return p

  path_1 = Entering("first")
  t = type_file(path_1)
  print(f"Your path is a {t}")
  path_2 = Entering("second", path_1, t)
  t2 = type_file(path_2)

  # Choose between spoting difference or intersection or both
  print("\n\nd: difference\ni: intersection\n[di, b]: both")
  choice = input("Spot the [D]ifference or [I]ntersection or [B]oth: ").lower()

  if choice == "b":
    Intersection()
    Diff(path_1, path_2, t, t2)
  elif choice == "i":
    Intersection()
  else:
    res = Diff(path_1, path_2, t, t2)
    if type(res) == str:
      print(res)
    else:
      for key, value in res.items():
        print(key, value)



def Designer():
  def Difference():
    path_1 = windows.Lp1.text() 
    path_2 = windows.Lp2.text()
    # if os.path.isdir("")  



  App = QApplication([])
  windows = loadUi("Designer/Files/1_Difference.ui")
  windows.show()
  windows.Bdiff.clicked.connect(Difference)


CLI()
# input
"""
/home/ghoudiy/Downloads/Temp/Test/Hello
/home/ghoudiy/Downloads/Temp/Test/Hallo
"""