t = int(input()) * 2

arr = []
for _ in range(t): 
    arr.append(list(map(str, input().split())))

def cleanWord(ch): 
    if len(ch) == 1:
        return ch
    if ch[0] == ch[1]: 
        return cleanWord(ch[1:])
    return ch[0] + cleanWord(ch[1:])

def distract(ch): 
    ok = True
    for i in range(len(ch)):  
        for j in range(i+1,len(ch)): 
            if ch[i] == ch[j]: 
                ok = False
                break
    return ok 



# for i in range(1,t,2): 
#     ch = cleanWord(arr[i][0])
#     if distract(ch):
#         print("YES")
#     else: 
#         print("NO")


# Or simply
for _ in range(1,t,2): 
    ch = arr[_][0]
    for i in range(len(ch)): 
        if ch[i] in ch[:i] and ch[i] != ch[i-1]: 
            print("NO")
            break
    else: 
        print("YES")
