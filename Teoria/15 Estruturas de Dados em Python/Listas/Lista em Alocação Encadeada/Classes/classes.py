class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def print(self):
        current = self.cabeca
        while current:
            print(current.valor)
            current = current.proximo

    # Atributo busca
    def busca(self, k):
        noAtual = self.cabeca
        if noAtual.chave == k:
            return noAtual               # Chave encontrada
        while noAtual.proximo != None:
            noAtual = noAtual.proximo    # Passe para próximo nó
            if noAtual.chave == k:
                return noAtual           # Chave encontrada
        return None                      # Chave não encontrada

    # Inserção no final da lista
    def insereFinal(self, novoNo):
        noAtual = self.cabeca
        if noAtual:                         # Caso a lista não esteja vazia
            while noAtual.proximo:
                noAtual = noAtual.proximo   # Busca no final da lista
            noAtual.proximo = novoNo
        else:                               # Caso a lista esteja vazia
            self.cabeca = novoNo

    # Inserção no início da lista
    def insereInicio(self, novoNo):
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo

    # Inserção em lista ordenada
    def insereOrdenada(self, novoNo):
        noAtual = self.cabeca                      # Início da busca da posição
        if noAtual.chave > novoNo.chave:
            novoNo.proximo = self.cabeca
            self.cabeca = novoNo                   # Insere no início
            return 0
        if noAtual.proximo != None:
            while (noAtual.chave < novoNo.chave):
                if (noAtual.proximo == None):
                    noAtual.proximo = novoNo       # Insere no final
                    return 0
                noAnterior = noAtual
                noAtual = noAtual.proximo          # Continue a busca
                # Fim da busca
        novoNo.proximo = noAtual                   # Apontar novo nó
        noAnterior.proximo = novoNo                # Inserir novo nó

    def removeLista(self, k):
        noAtual = self.cabeca
        if noAtual == None:
            return None
        if noAtual.chave == k:                            # Primeiro nó é o alvo
            self.cabeca = noAtual.proximo
            return 0
        noAnterior = noAtual                              # Continua a busca
        noAtual = noAtual.proximo
        while (noAtual != None):
            if noAtual.chave == k:                        # Chave encontrada
                noAnterior.proximo = noAtual.proximo      # Removeu o nó
                return k
            else:
                noAnterior = noAtual                      # Continua a busca
                noAtual = noAtual.proximo
        return -1                                         # Erro chave não encontrada
