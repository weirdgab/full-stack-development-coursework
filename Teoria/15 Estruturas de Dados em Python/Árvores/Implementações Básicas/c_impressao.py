from Classes.NoArvore import NoArvore


# Impressão da árvore implementada
def ImprimeArvoreRecurs(raiz, nivel=0):
    if raiz is None:
        return

    ImprimeArvoreRecurs(raiz.direita, nivel + 1)          # Imprime filhos à direita
    print(' ' * 4 * nivel + str(raiz.chave))

    ImprimeArvoreRecurs(raiz.esquerda, nivel + 1)         # Imprime filhos à esquerda


def ImprimeArvore(raiz):
    ImprimeArvoreRecurs(raiz)


print(ImprimeArvore(raiz))
