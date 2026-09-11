lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fTesteParidade(x): return x % 2 == 0


print(f'teste de fTesteParidade(5) = {fTesteParidade(5)}')

pares = list(filter(fTesteParidade, lista))

pares(f'lista de números pares = {pares}')
