from b_heranca_classe_exception import ExcecaoCustomizada


def checa_valor(valor):
    if valor < 0:
        raise ExcecaoCustomizada('Valor não pode ser negativo!')
