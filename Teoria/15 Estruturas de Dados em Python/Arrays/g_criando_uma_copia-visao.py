import numpy as np

nomes = np.array(['João', 'Maria', 'Ana'])

print(nomes)

visao = nomes.view()

visao[0] = 'Nelson'

print(nomes)
print(visao)