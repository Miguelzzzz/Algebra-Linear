import numpy as np

# 4) Multiplicação de Matrizes
# Considere:
# A = [[1,2],[3,4]]
# B = [[2],[1]]
# Tarefa:
# 1. - Ler A via input
# 2. - Ler B via input
# 3. - Calcular A * B
# 4. - Exibir resultado

A = np.array([
            [float(input()), float(input())], 
            [float(input()), float(input())], 
            ])

B = np.array([
            [float(input())],
            [float(input())],
            ])

multiplicacao = np.dot(A, B)

print("Resultado multiplicação:\n", multiplicacao)