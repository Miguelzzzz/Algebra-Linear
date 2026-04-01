import numpy as np

u = np.array(list(map(float, input("Digite os valores de u: ").split())))
v = np.array(list(map(float, input("Digite os valores de v: ").split())))

produtoEscalar = np.dot(u, v)

if np.isclose(produtoEscalar, 0):
    print("Força aplicada de forma eficiente")
else:
    print("Força desalinhada com a superfície")