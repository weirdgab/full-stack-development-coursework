from b_heranca_classe_exception import ExcecaoCustomizada
from c_metodo_checa_valor import checa_valor

try:
    checa_valor(-10)
except ExcecaoCustomizada as ex:
    print(f'Exceção lançada: {ex}')
