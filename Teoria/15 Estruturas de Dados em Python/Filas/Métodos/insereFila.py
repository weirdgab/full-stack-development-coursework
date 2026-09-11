maxFila = 10
fila = [None] * maxFila
inicioFila = None
finalFila = None


def insereFila(novoNo):
    global inicioFila                              # Indica o acesso a variáveis globais
    global maxFila
    global finalFila
    global fila
    if inicioFila == None:                        # Fila vazia
        fila[0] = novoNo                          # Insere o nó
        inicioFila = 0                            # Atualiza o início da fila
        finalFila = 0                             # Atualiza o final da fila
    elif (finalFila + 1) % maxFila == inicioFila:  # Fila cheia
        return -1                                 # -1 indica erro de fila cheia
    else:
        finalFila = (finalFila + 1) % maxFila     # Atualiza o final da fila
        fila[finalFila] = novoNo                  # Insere o nó
    return finalFila                              # Saída normal
