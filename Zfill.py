# zfill

import os 

path = input("Path: ")
while path.isdir() == False:
	path = input("Path: ")
os.chdir(path)

# List all files
L,S = [],[]
for file in os.listdir(): 
	if os.path.isfile(file):
	 L.append(file[1:file.find(" ")]),S.append(file)
print(S)

# Remove any non digit character
for j in range(len(L)):
	for i in range(len(L[j])): 
		if not L[j][i].isdecimal(): 
			L[j] = L[j][:i] + L[j][i+1:]
			
# zfill indices of files
L = list(map(lambda ch: ch.zfill(int(input("Give the width: ")), L))
for i in range(len(L)):
	dash = S[i].find("-") 
	name = S[i][0] + L[i] + " " + S[i][dash:]

	# Add space if not exist
	if S[i][dash + 1] != " ": 
		name = S[i][0] + L[i] + " " + S[i][dash] + " " + S[i][dash + 1:]

	if S[i] != name: 
		os.rename(S[i], name)

R = []
for file in os.listdir(): R.append(file)
print(sorted(R))
