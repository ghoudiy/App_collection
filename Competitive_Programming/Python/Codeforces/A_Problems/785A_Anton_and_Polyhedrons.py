n = int(input())

S = []

for _ in range(n):
    S.append(input())

nbf = 0
for i in range(n):
    if S[i] == "Tetrahedron":
        nbf += 4
    elif S[i] == "Cube":
        nbf += 6
    elif S[i] == "Octahedron": 
        nbf += 8
    elif S[i] == "Dodecahedron":
        nbf += 12
    elif S[i] == "Icosahedron":
        nbf += 20
print(nbf)