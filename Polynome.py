# -- Polynome --

from numpy import array

degree = int(input("Donner le degree: ")) + 1
while (2 >= degree):
    degree = int(input("Donner le degree: "))
T = array([int] * degree)
for i in range(degree):
    T[i] = int(
        input(f"{'c' if (degree - i - 1) == 0  else ('x' + str(degree - i - 1))}= "))
fx = float(input("Donner le racine: "))
racine = 0
k = 0
for i in range(degree):
    k += 1
    if (degree - k != 0):
        T[i] *= (fx ** (degree - k))
    racine += T[i]
if racine == 0:
    print(f"\n{int(fx)} est une racine de P")
else:
    print(f"{int(fx)} n'est pas une racine de P")
    polynome = [2, 1, 0.5, -0.5, -1, -2]
    k = 0
    for i in range(degree):
        k += 1
        if (degree - k != 0):
            T[i] /= (fx ** (degree - k))
    fx = []
    for rc in polynome:
        racine = 0
        k = 0
        for i in range(degree):
            k += 1
            if degree - k != 0:
                T[i] *= (rc ** (degree - k))
            racine += T[i]
        if racine == 0:
            fx.append(rc)
            if rc == 0.5:
                fx.append("1/2")
            elif rc == -0.5:
                    fx.append("-1/2")
        for i in range(degree):
            k += 1
            if degree - k != 0:
                T[i] /= (rc ** (degree - k))
    if len(fx) == 0:
        pass
    elif len(fx) > 1:
        print(f"{','.join(map(str, fx))} sont des racines de P")
    else:
        print(f"{','.join(map(str, fx))} est une racines de P")
