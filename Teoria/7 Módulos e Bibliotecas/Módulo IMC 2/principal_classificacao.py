from imc import calcula_imc
from imc_classificacao import classifica_imc

indice = calcula_imc(70, 1.80)
classificacao_imc = classifica_imc(indice)
print(f'Seu imc é {indice} e classificado como {classificacao_imc}')