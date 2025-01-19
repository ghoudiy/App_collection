t = int(input())

arr = []
for _ in range(t): 
    arr.append(list(map(int,input().split())))

for i in range(t): 
    hh = arr[i][0]
    mm = arr[i][1]
    print((23 - hh) * 60 + (60 - mm) if 24 - hh != 1 else 60 - mm)
