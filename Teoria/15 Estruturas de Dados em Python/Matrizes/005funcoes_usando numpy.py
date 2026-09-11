import numpy as np

numeros = np.array([[4, 13, 16], [5, 7, 1], [8, 10, 15]])
print(numeros)

minimo = numeros.min() # Retorna o valor mínimo entre todos os elementos da matriz
maximo = numeros.max() # Retorna o valor máximo entre todos os elementos da matriz
soma = numeros.sum() # Retorna a soma de todos os elementos da matriz
media = numeros.mean() # Retorna a média de todos os elementos da matriz
desvio = numeros.std() # Retorna o valor do desvio padrão de todos os elementos da matriz

print('Mínimo =', minimo)
print('Máximo =', maximo)
print('Média =', media)
print('Desvio =', desvio)