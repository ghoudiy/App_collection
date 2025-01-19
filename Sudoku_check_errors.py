"""
This is a program to check whether the given soduku is correct and to solve it if possible
"""

from random import randint
from copy import deepcopy


def Search(x, T, N):
	i = 0
	while (T[i] != x) and (i < N - 1):
		i += 1
	return T[i] == x


# Check soduku's matrix
def Correct(M, N):
	ok = True
	i = 0
	while (ok) and (i < N):
		j = 1
		while (ok) and (j < 10):
			ok = Search(j, M[i], N)
			j += 1
		i += 1
	return ok

# Check if number n is repeated in T
def Check(N, T, n, i):
	if n != 0 and T.count(n) > 1: # If number is repeated
		T[i] = 0
		tmp = [i] # Index of repeated number
		while n in T: 
			k = T.index(n)
			tmp.append(k)
			T[k] = 0
		N[f"{n = }"] = tmp

# Rotate Sudoku matrix (for checking columns)
def Rotate(M, N):
	Aux = deepcopy(M)
	for i in range(N-1):
		for j in range(i+1, N):
			Aux[i][j], Aux[j][i] = Aux[j][i], Aux[i][j]
	return Aux
	
# Update lines values (dictionary keys)
def Update_Lines(T, x):
	for dic in T: 
		R = {}
		for key in dic.keys():
			R[key] = f"{key[:-1]}{int(key[-1]) + x}"
		for old, new in R.items():
			dic[new] = dic.pop(old)

# Update columns values (dictionary values)
def Update_Columns(T, x):
	for dic in T: # Changes indexes (values)
		for key, value in dic.items():
			for k, v in value.items():
				for l in range(len(v)):
					dic[key][k][l] = v[l] + x
	
# Remove empty elements
rm_empty = lambda Y: list(filter(lambda x: len(x) > 0, Y))
 
# Check repeated numbers
def Check_numbers(M, N):
	Lines = [dict() for i in range(9)]   # [Line, [number, (indexes...)]]
	Columns = [dict() for i in range(9)] # [Column, [number, (indexes...)]]
	Mat = [dict() for i in range(45)] # [Line-Column, [number, (indexes...)]]
	Lx = 0
	Cx = 0
	Matx = 0
	ML = deepcopy(M)
	MC = Rotate(M, N)
	for i in range(N):
		L = dict()
		C = dict()
		for j in range(N):
			if j % 3 == 0 and i % 3 == 0 and N > 3: # Check 3*3 Matrixes
				Matrix = Check_numbers([M[l][j:j+3] for l in range(i, i+3)], 3)
				L1 = rm_empty(next(Matrix))
				C1 = rm_empty(next(Matrix))
				Update_Lines(L1, i)
				Update_Lines(C1, j)
				
				Update_Columns(L1, j)
				Update_Columns(C1, i)
			
				if len(L1) > 0 and len(C1) > 0:
					Mat[Matx][f"{i = }, {j = }"] = {"Line": L1, "Column": C1}
					Matx += 1
				elif len(L1) > 0:
					Mat[Matx][f"{i = }, {j = }"] = {"Line": L1}
					Matx += 1
				elif len(C1) > 0:
					Mat[Matx][f"{i = }, {j = }"] = {"Column": C1}
					Matx += 1
					
			Check(L, ML[i], ML[i][j], j) # Check Lines
			Check(C, MC[i], MC[i][j], j) # Check Columns

		if len(L) > 0:
			Lines[Lx][f"{i = }"] = L
			Lx += 1
		if len(C) > 0:
			Columns[Cx][f"j = {i}"] = C
			Cx += 1
		
	yield Lines
	yield Columns
	if N > 3:
		yield(rm_empty(Mat))
	
# Create Random Soduku
M = []
for i in range(9):
	# break
	M.append([randint(1,9) for _ in range(9)])

T = """
4 6 5 6 2 8 3 8 1
6 8 4 9 4 2 5 4 6
8 9 4 2 7 4 7 4 3
4 7 2 3 8 7 9 8 1
9 3 8 5 2 5 7 3 8
6 9 3 1 3 3 7 3 8
8 5 5 7 6 2 4 3 4
9 4 6 7 2 8 6 3 1
5 6 5 8 7 9 3 6 3
""".split("\n")[1:-1]
# M = [x.split() for x in T]
# M = [list(map(int, x)) for x in M]

[print(*M[i]) for i in range(9)]

Res = Check_numbers(M, 9)
print("#" * 50 + "\nMistakes in lines\n" + "\n".join(map(str, next(Res))))
print("-" * 50)
print("Mistakes in column\n" + "\n".join(map(str, next(Res))))
print("-" * 50)
print("Mistakes in matrix 3*3\n" + "\n".join(map(str, next(Res))))

"""
0 1 2 3 4 5 6 7 8

4 6 5 6 2 8 3 8 1  # 0
6 8 4 9 4 2 5 4 6  # 1
8 9 4 2 7 4 7 4 3  # 2
4 7 2 3 8 7 9 8 1  # 3
9 3 8 5 2 5 7 3 8  # 4
6 9 3 1 3 3 7 3 8  # 5
8 5 5 7 6 2 4 3 4  # 6
9 4 6 7 2 8 6 3 1  # 7
5 6 5 8 7 9 3 6 3  # 8
"""