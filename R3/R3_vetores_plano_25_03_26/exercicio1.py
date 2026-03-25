import numpy as np

posicaoInicial = np.array([2, 3, 3])
v1 = np.array([3, -1, 2])
v2 = np.array([-1, 4, 2])

soma = v1 + v2 + posicaoInicial

print("Posição final: ", soma)         