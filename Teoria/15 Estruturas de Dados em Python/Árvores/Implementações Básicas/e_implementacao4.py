from Classes.NoArvore import NoArvore
from c_impressao import ImprimeArvore, ImprimeArvoreRecurs
from d_funcoes_em_BST import inserirBST, buscaBST


if __name__ == '__main__':
    raiz = NoArvore(55)

    inserirBST(raiz, 35)
    inserirBST(raiz, 75)
    inserirBST(raiz, 25)
    inserirBST(raiz, 45)
    inserirBST(raiz, 65)
    inserirBST(raiz, 85)
    ImprimeArvore(raiz)
