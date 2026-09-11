import imc as c 
from imc_classificacao import classifica_imc as c_imc 

indice = c.calcula_imc(altura=1.88, peso=70)
classificacao_imc = c_imc(indice)