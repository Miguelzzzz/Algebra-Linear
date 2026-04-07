import numpy as np

u = np.array([3, 2])
v = np.array([1, 5])
w = np.array([8, 13])

A = np.column_stack((u, v))

try:
    coef = np.linalg.solve(A, w)
    a, b = coef

    print(f"a = {a}, b = {b}")

    if a != 0 and b != 0:
        print("w é uma combinação linear para os valores de a e b")
    else:
        print("não é combinação linear")

except np.linalg.LinAlgError:
    print("não é combinação linear")