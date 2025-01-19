t = int(input())

arr = []
for _ in range(t): 
    arr.append(list(map(int ,input().split())))

for i in range(t): 
    a = arr[i][0]
    b = arr[i][1]
    if a != b: 
        if a > b:
            nbc = (a - b) / 10
            print(int(nbc) if int(nbc) == nbc else int(nbc)+1)

        else: 
            nbc = (b - a) / 10
            print(int(nbc) if int(nbc) == nbc else int(nbc)+1)
    else:
        print(0)

"""
6
5 5
13 42
18 4
1337 420
123456789 1000000000
100500 9000
"""