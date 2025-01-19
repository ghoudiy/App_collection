import os
"""
We are giving a list of all variables
"""

def typ(t,ch): 
	print(ch, t, True, "#" * 20)
	# Simple type
	if t in ['int', 'int32', 'int64']: 
		return "entier"
	elif t in ['float', 'float32', 'float64']: 
		return "réel"
	elif t == "bool": 
		return "booléen"
	elif t == "str": 
		if len(str(ch)) == 1: 
			return "caractère"
		return "chaîne de caractère" # No need for else
	
	# Complex type
	elif t == "ndarray" or t == "list":
		if type(ch[0]).__name__ == "ndarray": # Matrice 
			ch1 = f"Tableau de {len(ch)} lignes et {len(ch[0])} colonnes des {typ(type(ch[0][0]).__name__, ch[0][0])}s"
			# ch1 = f"Tableau de {len(ch)}*{len(ch[0])} "
			# ch1 = f"Matrice de {len(ch)}*{len(ch[0])} "
			return ch1

		return f"Tableau de {len(ch)} {typ(type(ch[0]).__name__, ch[0])}s"
	
	elif t == "function":
		return "fonction"
	
def TDO(*Var):
	Var = list(Var)
	# ----------------------------------------------------------------
	# Some function Needed in program
	
	# Remove intersections of two lists
	def rem(L,R): 
		if L == R: 
			L = [x for x in L if x[:2] != "__"]
		else:
			for modu in " ".join(R).split(" "):
				if modu in L:
					L.remove(modu)
	
	# Sort element according to type
	def sor(ch):
		if type(eval(ch)).__name__ in ['int', 'float', 'bool', 'str']:
			return 0
		elif type(eval(ch)).__name__ in ["ndarray", "list"]:
			return 1
		else: 
			return 2

	# Remove all spaces or tabs
	def stri(c): 
		if c.find("\t") > -1:
			c = c.strip("\t")
		elif c.find(" ") > -1:
			c = c.strip(" ")
		return c

	# ----------------------------------------------------------------
	# Remove library functions
	rms = lambda ch,c="": ch.replace(",", c)
	L = open(__file__, encoding= "utf8").readlines()
	R = [stri(x) for x in L if x[0] != "#"]
	R = [x[7:] for x in R if x[:7] == "import " or x[:4] == "from"]		
	for i in range(len(R)): 
		if R[i].find(",") != -1: 
			R[i] = rms(R[i], " ")[:-1]
		else: 
			R[i] = rms(R[i])[:-1]
	rem(Var, R)

	# Remove TDO Function
	rem(Var, ["os", "TDO", "typ"])
	rem(Var, dir())
	Var = [x for x in Var if x[:2] != "__"] # Remove all built-in-functions start with "__"
	all_var = sorted(Var, key=sor)
	
	print("TDOG")
	# Check if there are variables in the program or not
	if len(all_var) > 0: 
		obj = f"  Object{' ' * (len(max(all_var, key=len)) + 3)}|   T/N\n"
		print(obj)
		for _ in range(len(all_var)): 
			t = type(eval(all_var[_])).__name__
			t = typ(t,eval(all_var[_]))
			ch = f"{' ' * 4}{all_var[_]}{' ' * (obj.find('|') - len(all_var[_]) - 4)}|  "
			if t != "fonction": 
				print(ch,t)
			else: # Module
				file = str(eval(all_var[_]).__code__)
				file = file[file.find('"')+1:]
				line = int(file[::-1][1:file[::-1].find(" ")][::-1]) - 1 # Line of module
				file = file[:file.find(', line ')-1] # File path 
				L = open(file, encoding="utf8").readlines()[line:] # Source code starting from the module above

				i = 0
				ok = True # Check if there is a return statement
				while (ok == True) and (i < len(L) - 1):
					i += 1
					if [L[1][0]] == ["\t"]:
						li = L[i].count("\t")
						l0 = L[0].count("\t")
						dash = L[i].strip("\t")[0] == "#"
					elif L[1][0] == " ":
						li = L[i].count(" ")
						l0 = L[0].count(" ")
						dash = L[i].strip(" ")[0] == "#"
					ok = ((li > l0) or (L[i] == "\n" or dash)) and L[i].find("return") == -1

				def Valid(ch): # Remove all special characters
					i = 0
					ok = True
					while (ok == True) and (i < len(ch)): 
						ok = "_,".find(ch[i]) != -1 or ch[i].isalnum()
						i += 1
					return ok

				# TDOL
				def TDOL(module,L, R, pf="Fonction"): # Tomorrow
					os.chdir(os.path.dirname(__file__))
					f = open(rf"TESTINGTDOGTDOL.py", "a", encoding="utf8")
					for k in range(len(L)):
						if stri(L[k])[5:] != "print" or str(L[k])[0] != "#":
							# f.write(L[k] + "\n")
							pass

					# f.write("\t" * (L[0].count("\t") + 1) + "print(dir())\n") # New information -> SyntaxError: f-string expression part cannot include a backslash				
					q = []
					if pf == "Procédure": 
						f = open("TESTINGTDOGTDOL.py", encoding="utf8").readlines()
						# print("Wait")
					elif pf == "Fonction": 
						for line in R:
							if line.find(module) != -1:
								ch2 = line[line.find(module):line.find(module)+len(module)]
								if len(ch2) > 0 and id(eval(ch2)) == id(eval(module)):
									# K = "".join(list(filter(Valid, line[line.find("(")+1:]))).split(",")
									K = line[line.find(module):]
									# K = K[:-1] + [K[-1][:-2]]
									q.append(stri(line))
					p = []
					for line in q: 
						test = line
						nb = 0
						while test.find(module):	
							if id(eval(test[test.find(module):test.find(module) + len(module)])) == id(eval(module)):
								nb += 1
							test = test[test.find(module)+len(module)+1:]
						while line.find(")") != -1:
							p.append(line[:line.find(")")])
							line = line[line.find(")") + 1:]
						print(nb, line)
					print(p)					
							
						# f.write(f"{module}(")

				# TDOL(all_var[_],L[0:i], L[i+1:])

				if ok == False and L[i].find("return") == -1:
					print(ch, "Procédure")
					#TDOL(all_var[_],L[0:i], L[i+1:], "Procédure")

				elif L[i].find("return") != -1: # if there are several variables in the return statement
					li = stri(L[i])[7:] # Vars in return statement
					if len(li.split(",")) > 1:
						print(ch, "Procédure")
						#TDOL(all_var[_],L[0:i], L[i+1:], "Procédure")

					else: # Fonction
						P = L[:i+1]
						ch1 = rms(stri(P[i]).strip("\n")[7::]) # Name of variable in return statement
						var = P[0][P[0].find("(")+1:]
						var = list(filter(Valid, var[:var.find(")")].split(","))) # List of all variables in def
						j = 1
						ok = False # Check if it is void or function (input - randint)
						while (ok == False) and (j <= len(P[1:i+1])):
							inpu = P[j].find("input")
							inpu = (inpu != -1 and inpu < max(P[j].find("'") + inpu+3, P[j].find('"') + inpu+3)) # P[j].find("'") + input => if there is no message
							rand = P[j].find("randint")
							rand = (rand != -1 and rand < max(P[j].find("'") + rand+3, P[j].find('"') + rand+3)) 
							ok = inpu or rand
							j += 1

						if (ok == True) and (ch1 not in var): 
							print(ch, "Procédure")
							#TDOL(all_var[_],L[0:i], L[i+1:], "Procédure")
						else: 
							
							print(ch, "Fonction")
							#TDOL(all_var[_],L[0:i], L[i+1:])

	else: # No variables
		print(f"  Object   |   T/N\n")

# TDO(*dir()) # Global