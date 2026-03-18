import numpy as np

u = np.array([1,2,3])
v = np.array([4,0,-1])

soma = u + v 
sub = u - v
escalar = 2 * u
modulo = np.linalg.norm(u)

print("Soma: U + v", soma)
print("Subtração: U - v", sub)
print("Escalar: 2 * U", escalar)
print("||U||: ", modulo)