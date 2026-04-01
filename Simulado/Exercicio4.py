import numpy as np

u = np.array([1, 4])
v = np.array([2, 1])
w = np.array([10, 8])

A = np.column_stack((u, v))

a, b = np.linalg.solve(A, w)

reconstrucao = a * u + b * v

print("a =", a)
print("b =", b)
print("Reconstrução:", reconstrucao)
print("É combinação linear:", np.allclose(reconstrucao, w))