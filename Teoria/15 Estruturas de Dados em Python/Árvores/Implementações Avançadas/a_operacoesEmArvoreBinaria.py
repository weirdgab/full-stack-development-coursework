from Classes.ArvoreBinaria import ArvoreBinaria

if __name__ == '__main__':
    arvore = ArvoreBinaria([12, 7, 7, 1, 3, 10])

print('Árvore:', arvore)

print('Tem 7 na árvore?', 7 in arvore)

arvore.addElemento(4)
print('Adicionando 4:', arvore)

arvore.removeElemento(3)
print('Removendo 3:', arvore)

arvore.addElementos([8, 40, 15, 68])
print('Adicionando vários elementos:', arvore)
