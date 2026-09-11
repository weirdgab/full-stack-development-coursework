maxPilha = 10
pilha = [None] * maxPilha
topoPilha = None


def push(novoNo):
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha == None:             # Pilha vazia
        pilha[0] = novoNo             # Insere o nó
        topoPilha = 0                 # Atualiza o topo da pilha
    elif (topoPilha == maxPilha - 1):    # -1 indica erro de pilha cheia
        return -1
    else:
        topoPilha = topoPilha + 1     # Atualiza o topo da pilha
        pilha[topoPilha] = novoNo     # Insere o nó
    return topoPilha                  # Saída normal


def pop():
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha == None:                   # Erro - pilha vazia
        return None                         # None indica erro pilha vazia
    else:
        k = pilha[topoPilha]                # Salva o nó removido
        if topoPilha == 0:
            topoPilha == None               # Pilha vazia após remoção
        else:
            topoPilha = topoPilha - 1       # Remove o nó
        return k                            # Retorne k = o nó consumido
