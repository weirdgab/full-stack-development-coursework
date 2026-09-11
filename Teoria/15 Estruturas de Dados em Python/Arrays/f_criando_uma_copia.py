import numpy as np

nomes = np.array(['João', 'Maria', 'Ana'])

print(nomes)

copia = nomes.copy()

copia[0] = 'Nelson'

print(nomes)
print(copia)

