# Mutabilidade
def sum(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print('\nSegundo Exemplo\n')
lista = ['ferrari']
lista.append('porsche')
print(lista)
