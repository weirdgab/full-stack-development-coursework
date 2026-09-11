# Gerar 1.000 pontos seguindo a distribuição normal
# Com média 20 e descio padrão 2
import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
print(dados)
plt.hist(dados, color = 'lightblue', ec = 'red')
plt.show()