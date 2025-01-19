def select(memory):
  memory : list= memory.split(", ")
  r = []
  ans = 0
  for mem in memory:
    if mem[0] == '!':
      ans += 1
      while mem[1:] in memory:
        memory.remove(mem[1:])
    else:
      if ans == 0:
        if f'!{mem}' not in memory:
          r.append(mem)
      else:
        while mem in r:
          r.remove(mem)
        memory.append(f"!{mem}")
        ans -= 1
  return ", ".join(r)


def select(memory):
  memory = memory.split(", ")
  r = []
  ans = 0
  for mem in memory:
    if mem[0] == '!':
      ans += 1
    else:
      if ans == 0:
        if f'!{mem}' not in memory:
          r.append(mem)
      else:
        while mem in r:
            r.remove(mem)
        memory.append(f"!{mem}")
        ans -= 1
  return ", ".join(r)

"""
'Nuerqjydp Upllmd, Heqtydlwaev Ugdoampr, Heqtydlwaev Ugdoampr, Heqtydlwaev Ugdoampr, Bucbme Wedfnf, Lrhvkghoe Dyuoybvdr, Czlcdjl Zvvmllvau, 
Bucbme Wedfnf, Iineicqn Nschesjhm, Lrhvkghoe Dyuoybvdr, !Czlcdjl Zvvmllvau, !Heqtydlwaev Ugdoampr, Iineicqn Nschesjhm, !Bofnplebwon Pysmgotrcsr, 
Iineicqn Nschesjhm, Bucbme Wedfnf, Nuerqjydp Upllmd, Lrhvkghoe Dyuoybvdr, Ypkvmef Smcgvhpmdf, Nuerqjydp Upllmd, 
Ypkvmef Smcgvhpmdf, !Yfllnxbh Oiyfflyxi, Ypkvmef Smcgvhpmdf, Iineicqn Nschesjhm'


'Nuerqjydp Upllmd, Lrhvkghoe Dyuoybvdr, Lrhvkghoe Dyuoybvdr, Nuerqjydp Upllmd, Lrhvkghoe Dyuoybvdr, Nuerqjydp Upllmd'
should equal
'Nuerqjydp Upllmd, Bucbme Wedfnf, Lrhvkghoe Dyuoybvdr, Bucbme Wedfnf, Lrhvkghoe Dyuoybvdr, Bucbme Wedfnf, Nuerqjydp Upllmd, Lrhvkghoe Dyuoybvdr, 
Nuerqjydp Upllmd'"""














print(select("Nuerqjydp Upllmd, Heqtydlwaev Ugdoampr, Heqtydlwaev Ugdoampr, Heqtydlwaev Ugdoampr, Bucbme Wedfnf, Lrhvkghoe Dyuoybvdr, Czlcdjl Zvvmllvau, Bucbme Wedfnf, Iineicqn Nschesjhm, Lrhvkghoe Dyuoybvdr, !Czlcdjl Zvvmllvau, !Heqtydlwaev Ugdoampr, Iineicqn Nschesjhm, !Bofnplebwon Pysmgotrcsr, Iineicqn Nschesjhm, Bucbme Wedfnf, Nuerqjydp Upllmd, Lrhvkghoe Dyuoybvdr, Ypkvmef Smcgvhpmdf, Nuerqjydp Upllmd, Ypkvmef Smcgvhpmdf, !Yfllnxbh Oiyfflyxi, Ypkvmef Smcgvhpmdf, Iineicqn Nschesjhm"))