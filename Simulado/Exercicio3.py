import numpy as np

u = np.array([4, 3, 2])
v = np.array([1, 2, 1])

produtoEscalar = np.dot(u, v)
normaV2 = np.dot(v, v)

projecao = (produtoEscalar / normaV2) * v

print ("Produto escalar: ", produtoEscalar)
print ("||v||2: ", normaV2)
print ("Projeção: ", projecao)

if produtoEscalar > 0:
    print("Ajuda")
elif np.isclose(produtoEscalar, 0):
    print("Pouco eficiente")
else:
    print("Inútil")