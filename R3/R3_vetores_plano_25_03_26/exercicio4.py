import numpy as np

u = np.array([2, 1, 5])
v = np.array([1, 3, 4])
w = np.array([5, 4, 0])

A = np.array([[2, 1],
              [1, 3],
              [5, 4]])

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