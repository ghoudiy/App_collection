def do_sort(names):
  names = list(filter(lambda s: s[0].lower() == 'a', names))
  l = len(names)
  for i in range(l):
    Min = i
    for j in range(i + 1, l):
      if names[Min][0] == 'A' and names[j][0] == 'a': 
        Min = j
      if names[Min][0] == names[j][0] and (len(names[Min]) > len(names[j]) or (len(names[Min]) == len(names[j]) and names[Min] < names[j])):
        Min = j
    if i != Min:
      names[i], names[Min] = names[Min], names[i]
  return names
# Test Cases
print(do_sort(["Ameer", "alsayed", "Mahmoud", "Ahmed", "ayman", "Israa", "Anas", "amal", "amr", "aml"]))
print(do_sort(["Amir", "Ahmed", "amal", "ayoub", "aya", "Amine", "Achraf", "Ayman", "Lotfi", "amjad", "ahm"]))
# ['amr', 'aml', 'amal', 'ayman', 'alsayed', 'Anas', 'Ameer', 'Ahmed']
