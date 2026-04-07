import numpy as np

u = np.array(list(map(float, input().split())))
v = np.array(list(map(float, input().split())))

produtoEscalar = np.dot(u, v)

if np.isclose(produtoEscalar, 0):
    print("Força aplicada de forma eficiente")
else:
    print("Força desalinhada com a superfície")