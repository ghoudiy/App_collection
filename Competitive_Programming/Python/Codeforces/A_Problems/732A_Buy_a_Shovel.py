k,r = list(map(int, input().split()))

nbc = 1
j = k
while j % 10 != 0 and j % 10 != r: 
    nbc += 1
    j += k
print(nbc)

