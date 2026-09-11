from Classes.NoArvore import NoArvore


#  Estratégia recursiva
def visitaPreOrdem(raiz):
    if raiz:
        print(raiz.chave)
        visitaPreOrdem(raiz.esquerda)
        visitaPreOrdem(raiz.direita)
