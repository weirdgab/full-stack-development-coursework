from No import No


class DequeEncadeada:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

    # Atributo de busca
    def buscaDeque(self, k, L, n):
        i = 0
        indice = -1
        while i < n:
            if L[i] == k:
                indice = i
                i = n + 1
            i = i + 1
        return indice

    # Atributo de inserção
    def pushFront(self, novoNo):
        if self.inicio == None:           # Deque vazio
            self.inicio = novoNo          # Atualiza o início do deque
            self.final = novoNo           # Atualiza o final do deque
        else:
            self.final.proximo = novoNo   # Insere o nó
            self.final = novoNo

    # Atributo de inserção
    def pushBack(self, novoNo):
        novoNo.proximo = self.topo             # Insere o nó
        self.topo = novoNo                     # Atualiza o topo do deque

    def popFront(self):
        if self.topo == None:
            return None                        # Erro deque vazio
        k = self.topo                          # Salva o nó removido
        self.topo = self.topo.proximo          # Remove o nó
        return k                               # Retorna o nó removido

    def popBack(self):
        if self.inicio == None:                      # Erro - deque vazio
            return None                              # None indica erro deque vazio
        else:
            k = self.final                           # Salva o nó removido
            self.final = self.final.anterior         # Remove o nó
            self.final.proximo = None                # Aponta o próximo do final para λ
        return k                                     # Retorne k = o nó consumido
