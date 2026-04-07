import numpy as np

u = np.array([5, 4])
v = np.array([2, 1])

produtoEscalar = np.dot(u, v)
print("Produto escalar:", produtoEscalar)

if np.isclose(produtoEscalar, 0):
    print("Os vetores são ortogonais")
else:
    print("Os vetores não são ortogonais")
    
    projecao = (np.dot(u, v) / np.dot(v, v)) * v
    componenteParalelo = projecao
    componentePerpendicular = u - projecao

    print("Componente Paralelo (projeção):", componenteParalelo)
    print("Componente Perpendicular (erro):", componentePerpendicular)