
import os


def mv(name, path):
    os.chdir(path)
    Files = []
    for file in os.listdir():
        Files.append(file)
    Files.sort()

    if name in Files:
        # Check how many files exists with the same name
        def distinct(ch, ch1):
            i = 0
            ok = True
            while (ok == True) and (i < len(ch)):
                ok = ch[i] == ch1[i]
                i += 1
            return i
        
        N = []
        for file in Files:
            i = distinct(name, file)
            if file != name: 
                print(file[i+1:file.find(")")], "    |   ",
                      file[i+1:][file[i+1:].find(")")+1:])
                if file[:i-1] == name[:i-1] and file[i] == "(" and file[i+1:file.find(")")].isdigit() and (file[i+1:][file[i+1:].find(")")+1:] == name[i-1:]):
                    N.append(int(file[i+2]))
                    break
        
        # Check if there are missed numbers in files's names
        print(N)
        def Miss_Num(N):
            L = []
            for i in range(len(N)-1):
                if N[i+1] - N[i] != 1:
                    while N[i] != N[i+1]:
                        N[i] += 1
                        L.append(N[i])
            return L
        Num = Miss_Num(N)

        # Rename
        if len(Num) == 0:
            if len(N) > 0:
                num = sorted(N)[-1] + 1
            else:
                num = 1
        else:
            num = N[0]
        name1 = name[::-1][name[::-1].find(".")+1:][::-1] + \
            f" ({num})" + name[::-1][:name[::-1].find(".")+1][::-1]
        return name1

    else:
        return name


def Run():
    # Check if path exist
    def direction(dire):
        while dire[0] in ['"', "'"]:
            dire = dire[1:]
        while dire[-1] in ['"', "'"]:
            dire = dire[:-1]
        while os.path.isdir(dire) == False:
            dire = input("Path: ")
        return dire

    # Enter the path
    # dire = input("Path: ")
    dire = r"Y:\New Files\Test"
    if dire == "": 
        dire = os.getcwd()
    else: 
        dire = direction(dire)

    # Enter the name
    # name = input("File name: ")
    name = "yass.txt"
    while name == "":
        name = input("File name: ")

    # Program
    new_name = mv(name,dire)
    print(new_name)
    # open(f"{dire}/{new_name}", "a")

# Run()

def Recherche(folder, file): 
	L = os.listdir(folder)
	R = []
	for filename in os.listdir(folder): 
		def distinct(ch, ch1): 
			i = 0
			ok = True
			while (ok == True) and (i < len(ch)):
				ok = ch[i] == ch1[i]
				i += 1  
			return i

		ch = mv(file, os.path.abspath(folder))
		i = distinct(file, ch)
		if filename != file:  # filename (num)
			name = filename.split(" - Copie")
			if file[:i-1] == filename[:i-1] and filename[i] == "(" and filename[i+1].isdigit() and (filename[i+2] == ")" or filename[i+3] == ")") and (filename[i+3:] == file[i-1:] or filename[i+4:] == file[i-1:]):
				R.append(filename)
			elif name[0] == file[:i-1] and name[-1] == file[i - 1:] :
				R.append(filename)
		else:
			R.append(filename)
		
	return R

os.chdir("/home/ghoudiy/")
# file = input("File name: ")
file = "yass.txt"



# Files = Recherche(os.getcwd(), file)
# print(Files)
# if len(Files) == 0: 
# 	print("File is not exist")

# elif len(Files) > 1: 
# 	L = []
# 	for i in range(len(Files)): 
# 		ch = Files[i][:Files[i].find("Programming")-1][::-1]
# 		ch = "." + ch[:ch.find("/")+1][::-1]
# 		L.append(ch + Files[i][Files[i].find("Programming")+11:]) 
		
# 	fold = int(input(f"Index of the folder (0,{len(Files)-1}): ")) - 1
# 	while fold not in range(0,len(Files)):
# 		fold = int(input("Index=: ")) - 1
# 	else: 
# 		print(Files[fold])

# exec(open(f"'/home{Files[fold][1:]}'", 'r').read())
# print(os.path.exists(f"/home{Files[fold][1:]}"))
