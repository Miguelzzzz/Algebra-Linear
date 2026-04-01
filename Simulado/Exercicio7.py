import numpy as np

u = np.array([4, -2])
v = np.array([1, 2])

produtoEscalar = np.dot(u, v)

if np.isclose(produtoEscalar, 0):
    print("Rota segura")
else:
    print("Rota perigosa")