from Classes.NoArvore import NoArvore


def visitaEmOrdem(raiz):
    if raiz:
        visitaEmOrdem(raiz.esquerda)
        print(raiz.chave)
        visitaEmOrdem(raiz.direita)
