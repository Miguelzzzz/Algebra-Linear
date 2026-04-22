import numpy as np

# 1) Soma de Matrizes
# Considere:
# A = [[1,2],[3,4]]
# B = [[5,6],[7,8]]
# Tarefa:
# 1. - Criar A e B com numpy
# 2. - Ler os elementos da matriz A via input
# 3. - Ler os elementos da matriz B via input
# 4. - Calcular A + B
# 5. - Exibir o resultado
# Exemplo de código:
# import numpy as np

A = np.array([[float(input()), float(input())], [float(input()), float(input())]])

B = np.array([[float(input()), float(input())], [float(input()), float(input())]])

soma = np.add(A, B)

print("Soma das Matrizes", soma)