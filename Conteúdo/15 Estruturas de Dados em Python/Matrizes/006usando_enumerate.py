import numpy as np

numeros = np.array([[4, 13, 16], [5, 7, 1], [8, 10, 15]])
print(numeros)

# Criando cópia numerada com enumerate
for indice, valor in enumerate(numeros):
    print(indice, valor)