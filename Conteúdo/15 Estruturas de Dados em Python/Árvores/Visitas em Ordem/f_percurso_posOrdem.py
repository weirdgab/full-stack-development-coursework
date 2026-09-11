from Classes.NoArvore import NoArvore


def VisitaPosOrdem(raiz):
    if raiz:
        VisitaPosOrdem(raiz.esquerda)
        VisitaPosOrdem(raiz.direita)
        print(raiz.chave)
