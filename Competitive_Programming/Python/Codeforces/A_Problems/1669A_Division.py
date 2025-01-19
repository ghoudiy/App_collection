t = int(input())

ar = []
for _ in range(t): 
    ar.append(int(input()))

for i in range(t): 
    rating = ar[i]
    div = "Division"
    if rating >= 1900: 
        print(div, 1)
    elif 1899 >= rating >= 1600: 
        print(div, 2)
    elif 1599 >= rating >= 1400:
        print(div, 3)
    else: 
        print(div, 4)