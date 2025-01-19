t = int(input())

arr = []
for i in range(t): 
    arr.append(list(map(int, input().split())))

for i in range(t): 
    x,y,n = arr[i][0],arr[i][1],arr[i][2]
    
    # Or directly 
    print(n - (n - y) % x)

    # Accepted
     
    # if n % x != y: 
    #     a = n // x 
    #     k = (a * x) + y
    #     while k % x != y or k >= n: 
    #         a -= 1
    #         k = (a * x) + y
    #     print(k)
    # else: 
    #     print(n)