class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = self.inicio

    # Atributo de busca
    def busca(self, k):
        noAtual = self.inicio
        if noAtual.chave == k:
            return noAtual
        while noAtual.proximo != None:
            noAtual = noAtual.proximo
            if noAtual.chave == k:
                return noAtual
        return None

    # Atributo de inserção
    def insere(self, novoNo):
        if self.inicio == None:           # Fila vazia
            self.inicio = novoNo          # Atualiza o início da fila
            self.final = novoNo           # Atualiza o final da fila
        else:
            self.final.proximo = novoNo   # Insere o nó
            self.final = novoNo           # Atualiza o final da fila

    # Atributo de remoção
    def remove(self):
        if self.inicio == None:                       # Erro - fila vazia
            return None                               # None indica erro fila vazia
        else:
            k = self.inicio                           # Salva o nó removido
            self.inicio = self.inicio.proximo         # Remove o nó
            return k                                  # Retorne k = o nó consumido
