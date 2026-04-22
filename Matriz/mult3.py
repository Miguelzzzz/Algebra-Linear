import numpy as np

# 5) Multiplicação de Matrizes (2x3 · 3x2)
# Considere:
# A = [[1,0,2],
#     [-1,3,1]]

# B = [[2,1],
#       [0,3],
#       [1,-1]]
# Tarefa:
# 1. - Ler todos os elementos via input
# 2. - Montar as matrizes
# 3. - Calcular A * B
# 4. - Exibir resultado

A = np.array([
            [float(input()), float(input()), float(input())], 
            [float(input()), float(input()), float(input())], 
            ])

B = np.array([
            [float(input()), float(input())], 
            [float(input()), float(input())], 
            [float(input()), float(input())], 
            ])

mult = np.dot(A, B)

print("A multiplicação de matrizes \n", mult)