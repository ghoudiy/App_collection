ch = input()

R = ""
while len(ch) > 0: 
    i = 0
    if ch[i] == "-" and ch[i+1] == "-": 
        R += "2"
        ch = ch[:i] + ch[i+2:]
    elif ch[i] == "-" and ch[i+1] == ".":
        R += "1"
        ch = ch[:i] + ch[i+2:]
    else: 
        R += "0"
        ch = ch[:i] + ch[i+1:]
print(R)
