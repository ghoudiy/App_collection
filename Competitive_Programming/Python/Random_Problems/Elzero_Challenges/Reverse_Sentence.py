# Method 1

def rever(ch):
    ch = ch.split(" ")
    ch.reverse()
    return " ".join(ch)

print(rever("Elzero Web School"))
print(rever("Yassine Ghoudi Hello"))
# print(rever(input("Word to reverse: ")))

# Method 2 : 
def rever2(ch):
    ch = ch[::-1]
    ch1 = ""
    long = len(ch)
    while len(ch1) != long:
        ch1 += ch[:ch.find(" ")][::-1] + " " if ch.find(" ") != -1 else ch[::-1]
        ch = ch[ch.find(" ")+1:]
    return ch1

print(rever2("Elzero Web School"))
print(rever2("Yassine Ghoudi Hello"))
