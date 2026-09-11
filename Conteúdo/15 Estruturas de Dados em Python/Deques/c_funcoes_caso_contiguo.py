maxDeque = 10
deque = [None] * maxDeque
inicioDeque = None
finalDeque = None


def pushFront(novoNo):
    global deque
    global finalDeque
    global maxDeque
    if finalDeque == None:                # Deque vazio
        deque[0] = novoNo                 # Insere o nó
        finalDeque = 0                    # Atualiza o final do deque
    elif (finalDeque == maxDeque - 1):    # -1 indica erro de deque cheio
        return -1
    else:
        finalDeque = finalDeque + 1       # Atualiza o final do deque
        deque[finalDeque] = novoNo        # Insere o nó
    return finalDeque                     # Saída normal


def pushBack(novoNo):
    global inicioDeque                                # Indica o acesso a variáveis globais
    global maxDeque
    global finalDeque
    global fila
    if inicioDeque == None:                           # Deque vazio
        fila[0] = novoNo                              # Insere o nó
        inicioDeque = 0                               # Atualiza o início do deque
        finalDeque = 0                                # Atualiza o final do deque
    elif (finalDeque + 1) % maxDeque == inicioDeque:  # Deque cheio
        return -1                                     # -1 indica erro de deque cheio
    else:
        finalDeque = (finalDeque + 1) % maxDeque       # Atualiza o final do deque
        deque[finalDeque] = novoNo                     # Insere o nó
    return finalDeque                                  # Saída normal


def popFront():
    global deque
    global finalDeque
    global maxDeque
    if finalDeque == None:                    # Erro - deque vazio
        return None                           # None indica erro deque vazio
    else:
        k = deque[finalDeque]                 # Salva o nó removido
        if finalDeque == 0:
            finalDeque == None                # Deque vazia após remoção
        else:
            finalDeque = finalDeque - 1       # Remove o nó
        return k                              # Retorne k = o nó consumido


def popBack():
    global inicioDeque                                  # Indica o acesso a variáveis globais
    global maxDeque
    global finalDeque
    global deque
    if inicioDeque == None:                             # Deque vazia
        return None                                     # Erro deque vazia
    k = deque[inicioDeque]                              # Salva o nó removido
    if finalDeque == inicioDeque:
        inicioDeque = None                              # Deque vazia após remoção
    else:
        finalDeque = (finalDeque - 1) % maxDeque        # Remove o nó
    return k                                            # Retorne k = o nó consumido
