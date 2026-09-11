from Classes.NoArvore import NoArvore


# Função de busca
def buscaBST(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    else:
        if raiz.chave < chave:
            return buscaBST(raiz.direita, chave)
        elif raiz.chave > chave:
            return buscaBST(raiz.esquerda, chave)
        else:
            raiz


# Função de inserção
def inserirBST(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    else:
        if raiz.chave == chave:
            return raiz
        elif raiz.chave < chave:
            reiz.direita = inserirBST(raiz.direita, chave)
        else:
            raiz.esquerda = inserirBST(raiz.esquerda, chave)
    return raiz


# Função de deleção
def deleteBST(raiz, chave):
    if raiz is None:
        return raiz
    if chave < raiz.chave:
        raiz.esquerda = deleteBST(raiz.esquerda, chave)
    elif (chave > raiz.chave):
        raiz.direita = deleteBST(raiz.direita, chave)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda
            raiz = None
            return temp
        temp = valorNo(raiz.direita)
        raiz.chave = temp.chave
        raiz.direita = deleteBST(raiz.direita, temp.chave)
    return raiz


# Função de auxílio para deleção de nós
def valorNo(no):
    atual = no
    while (atual.esquerda is not None):
        atual = atual.esquerda
    return atual
