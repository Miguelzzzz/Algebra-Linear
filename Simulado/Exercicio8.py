import numpy as np

u = np.array([3, 2])
v = np.array([1, 5])
w = np.array([8, 13])

A = np.array([[3, 1],
              [2, 5]])

a, b = np.linalg.solve(A, w)

print("a =", a)
print("b =", b)

wCalculado = a * u + b * v

if np.isclose(wCalculado, w):
    print("w É uma combinação linear para os valores de a e b")
else:
    print("Não é combinação linear")