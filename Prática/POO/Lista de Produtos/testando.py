from Funções.buscaLista import buscaLista
from Funções.removeLista import removeLista
from Funções.insereLista import insereLista

produtos = ['Laranja', 'Palmito', 'Feijão']

clientes = ['Ana Pera', 'João Silva', 'Maria Santos']

print('Lista produtos sem alteração: {}\n'.format(produtos))
print('Lista clientes sem alteração: {}\n'.format(clientes))

print('Buscando primeiro ítem da lista produtos: ',
      buscaLista('Laranja', produtos, len(produtos)))
print('Buscando primeiro ítem da lista clientes: ',
      buscaLista('Ana Pera', clientes, len(clientes)), '\n')

print('Removendo o segundo ítem da lista produtos...')
removeLista('Palmito', produtos, len(produtos))
print('Removendo o segundo ítem da lista clientes...')
removeLista('João Silva', clientes, len(clientes))
print('\n')

print('Lista produtos após remoção: ', produtos)
print('Lista clientes após remoção: ', clientes, '\n')

print('Inserindo ítem "banana" a lista produtos... ')
insereLista('Banana', produtos, len(produtos))
print('Inserindo ítem "Gabriel" a lista clientes...')
insereLista('Gabriel', clientes, len(clientes))
print('\n')

print('Lista produtos após inserção: ', produtos)
print('Lista clientes após inserção: ', clientes, '\n')
