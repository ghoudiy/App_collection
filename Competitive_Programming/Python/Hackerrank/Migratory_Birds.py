arr_count = int(input())

ar = list(map(int,input().split()))

# Internet

count = [0] * 6

for bird in ar:
    count[bird] += 1

print (count.index(max(count)))

    

    
"""
if today == hammaBirthday: 
    print("Happy Birthday!")
else: 
    print("Wa9teh 3id miledk bech m3ach na8ltou")
"""