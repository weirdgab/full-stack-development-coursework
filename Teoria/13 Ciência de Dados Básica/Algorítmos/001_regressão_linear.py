# Algorítmo supervisionado

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas
import os

############ Pré-processamento ############
# Coleta e Integração
# Garante que acha o arquivo na mesma pasta do script
caminho = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'dados_dengue.csv')
arquivo = pandas.read_csv(caminho)

anos = arquivo[['ano']]
casos = arquivo[['casos']]

############ Mineração ############
regr = LinearRegression()
regr.fit(X=anos, y=casos)

# Correção do Warning 1: Usando DataFrame para prever, igual ao treino
ano_futuro_df = pandas.DataFrame([[2018]], columns=['ano'])
casos_2018 = regr.predict(ano_futuro_df)

# Correção do Warning 2: Convertendo array para número corretamente antes de imprimir
print('Casos previstos para 2018 ->', int(casos_2018[0][0]))

############ Pós-processamento ############
# Gráfico dos dados originais
plt.scatter(anos, casos, color='black')

# Gráfico do ponto previsto (vermelho)
# Convertemos para lista simples para o gráfico não reclamar
plt.scatter(ano_futuro_df, casos_2018, color='red')

# Linha da regressão (azul)
plt.plot(anos, regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2018])

plt.show()
