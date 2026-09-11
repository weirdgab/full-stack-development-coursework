lista = [10, 20, 30, 40, 50]
print(f'A lista inicial é: {lista}')

# Removendo um elemento da lista
lista.remove(40) # Remove o primeiro valor 40 encontrando
print(f'Lista após remover 40: {lista}')

# Removendo o último elemento da lista
ultimo_elemento = lista.pop()
print(f'Lista após remover o último elemento: {lista}')
print(f'Elemento removido: {ultimo_elemento}')