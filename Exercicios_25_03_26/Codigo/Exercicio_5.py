import numpy as np

u = np.array([3, 1])
v = np.array([4, 2])

prodEscalar = np.dot(u, v)

normU = np.linalg.norm(u)
normV = np.linalg.norm(v)
cosTheta = prodEscalar / (normU * normV)

anguloGraus = np.degrees(np.arccos(cosTheta))

print(f"Produto Escalar: {prodEscalar}")
print(f"Cos(theta): {cosTheta:.4f}")
print(f"Ângulo: {anguloGraus:.2f}°")