import numpy as np

# 3) Multiplicação por Escalar
# Considere:
# A = [[3,-2],[1,4]]
# Tarefa:
# 1. - Ler a matriz A via input
# 2. - Ler o escalar k
# 3. - Calcular KA
# 4. - Exibir resultados

A = np.array([
            [float(input()), float(input())], 
            [float(input()), float(input())], 
            ])

prodEscalar = float(input())

mult = np.dot(A, prodEscalar)

print("Multiplicação Escalar \n", mult)