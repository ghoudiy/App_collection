n = int(input())

while not (1 <= n <= 100):
    n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

nbm = 0

for i in range(n):
    p = arr[i][0]
    q = arr[i][1]
    if (q - p >= 2):
        nbm += 1
    
print(nbm)
        
