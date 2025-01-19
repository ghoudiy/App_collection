t = int(input()) * 2

arr = []
for i in range(t): 
    arr.append(list(map(int, input().split())))

def Tri_Bulle(L): 
    ok = True
    while ok == True:
        ok = False
        for i in range(len(L)-1): 
            if L[i] > L[i+1]: 
                Aux = L[i+1]
                L[i+1] = L[i]
                L[i] = Aux
                ok = True

for i in range(1,t,2):
    S = set(arr[i])
    if len(S) == 1: 
        arr[i] = [1]
    else: 
        Tri_Bulle(arr[i])
        n = arr[i-1][0]
        j = 0
        ok = True
        while ok == True and j <= n - 1: 
            # print('-' * 50)
            # print(arr[i])
            # print("[arr[i][j], arr[i][j+1]]=",arr[i][j], arr[i][j+1])
            if abs(arr[i][j] - arr[i][j+1]) <= 1: 
                # print(True)
                if arr[i][j] < arr[i][j+1]:
                    arr[i].remove(arr[i][j])
                    j -= 1
                else:
                    arr[i].remove(arr[i][j+1])
                    j -= 1
            
            else: 
                ok = False

            S = set(arr[i])
            if len(S) == 1:
                ok = False 
            j += 1

for i in range(1,t,2): 
    S = set(arr[i])
    print("YES" if len(S) == 1 else "NO")
