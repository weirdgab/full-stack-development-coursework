maxFila = 10
fila = [None] * maxFila
inicioFila = None
finalFila = None


def removeFila():
    global inicioFila                             # Indica acesso as variáveis globais
    global maxFila
    global finalFila
    global fila
    if inicioFila == None:                        # Fila vazia
        return None                               # Erro fila vazia
    k = fila[inicioFila]                          # Salva o nó removido
    if finalFila == inicioFila:
        inicioFila = None                         # Fila vazia após remoção
    else:
        inicioFila = (inicioFila + 1) % maxFila   # Remove o nó
    return k                                      # Retorne k = o nó consumido
