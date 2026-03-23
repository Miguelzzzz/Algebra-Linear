import numpy as np

u = np.array([3, 2])
v = np.array([1, -1])
w = np.array([5, 1])

A = np.array([[3, 1],
              [2, -1]])

a, b = np.linalg.solve(A, w)

print("a =", a)
print("b =", b)

wCalculado = a * u + b * v

print("w calculado:", wCalculado)
print("w original:", w)

if np.allclose(wCalculado, w):
    print("w Pode ser escrito como combinação linear de u e v")
else:
    print("w Não pode ser escrito como combinação linear de u e v")