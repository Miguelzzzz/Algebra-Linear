import numpy as np

u = np.array([7, 2])
v = np.array([1, 3])

produtoEscalar = np.dot(u, v)

print("Produto escalar:", produtoEscalar)

if np.isclose(produtoEscalar, 0):
    print("Ortogonal: sim")
    print("Projeção:", np.array([0, 0]))
    print("Interpretação: inútil / perpendicular")
else:
    print("Ortogonal: não")
    projecao = (produtoEscalar / np.dot(v, v)) * v
    print("Projeção de u sobre v:", projecao)
    
    if np.allclose(projecao, 0):
        print("Interpretação: inútil / perpendicular")
    elif np.linalg.norm(projecao) < 1:
        print("Interpretação: baixa eficiência")
    else:
        print("Interpretação: movimento útil")