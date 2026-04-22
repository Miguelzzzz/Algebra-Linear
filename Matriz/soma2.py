import numpy as np

# 2) Soma de Matrizes 3x3
# Considere:
# A = [[2,0,1],[-1,3,2],[4,1,0]]
# B = [[1,5,2],[2,-3,1],[0,4,3]]
# Tarefa:
# 1. - Ler A e B via input
# 2. - Calcular A + B
# 3. - Exibir resultado

A = np.array([
            [float(input()), float(input()), float(input())], 
            [float(input()), float(input()), float(input())], 
            [float(input()), float(input()), float(input())]
            ])

B = np.array([
            [float(input()), float(input()), float(input())], 
            [float(input()), float(input()), float(input())], 
            [float(input()), float(input()), float(input())]
            ])

soma = np.add(A, B)

print("Soma das Matrizes \n", soma)