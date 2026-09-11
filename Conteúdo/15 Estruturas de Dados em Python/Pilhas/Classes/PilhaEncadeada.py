class PilhaEncadeada:
    def __init__(self, topo=None):
        self.topo = topo

    # Atributo de busca
    def buscaPilha(self, k, L, n):
        i = 0
        indiceL = -1
        while i < n:
            if L[i] == k:
                indiceL = i
                i = n + 1
            i = i + 1
        return indiceL

    # Atributo de inserção
    def push(self, novoNo):
        novoNo.proximo = self.topo             # Insere o nó
        self.topo = novoNo                     # Atualiza o topo da pilha

    # Atributo de remoção
    def pop(self):
        if self.topo == None:
            return None                        # Erro pilha vazia
        k = self.topo                          # Salva o nó removido
        self.topo = self.topo.proximo          # Remove o nó
        return k                               # Retorna o nó removido
