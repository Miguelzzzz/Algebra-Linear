import numpy as np

u = np.array([3, 1])
v = np.array([4, 2])

prod_escalar = np.dot(u, v)

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
cos_theta = prod_escalar / (norm_u * norm_v)

angulo_graus = np.degrees(np.arccos(cos_theta))

print(f"Produto Escalar: {prod_escalar}")
print(f"Cos(theta): {cos_theta:.4f}")
print(f"Ângulo: {angulo_graus:.2f}°")