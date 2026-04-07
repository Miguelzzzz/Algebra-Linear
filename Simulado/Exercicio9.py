import numpy as np

u = np.array([3, 2, 4])
v = np.array([4, 1, 2])

produtoEscalar = np.dot(u, v)

modU = np.linalg.norm(u)
modV = np.linalg.norm(v)

cos_theta = produtoEscalar / (modU * modV)
cos_theta = np.clip(cos_theta, -1.0, 1.0)

anguloRad = np.arccos(cos_theta)
anguloGraus = np.degrees(anguloRad)

print(f"Produto escalar: {produtoEscalar}")
print(f"Módulo de u: {modU:.2f}")
print(f"Módulo de v: {modV:.2f}")
print(f"Ângulo (rad): {anguloRad:.4f}")
print(f"Ângulo (graus): {anguloGraus:.2f}")

if anguloGraus < 30:
    print("Vetores bem alinhados")
elif anguloGraus < 80:
    print("Vetores parcialmente alinhados")
elif anguloGraus < 100:
    print("Vetores quase ortogonais")
else:
    print("Vetores em direções opostas")