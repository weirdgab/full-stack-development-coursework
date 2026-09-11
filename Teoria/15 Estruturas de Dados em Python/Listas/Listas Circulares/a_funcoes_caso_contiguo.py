def insereCircular(novoNo):
    if inicioLista == None:                 # Lista vazia
        inicioLista = novoNo
        finalLista = novoNo
        novoNo.proximo.novoNo
    else:
        finalLista.proximo = novoNo         # Insere o nó
        finalLista = novoNo                 # Atualiza ponteiros
        finalLista.proximo = inicioLista


def removeCircular(k):
    noAnterior = buscarAnterior(k)                  # Busca o nó anterior ao que será removido
    if noAnterior == None:
        return None                                 # Erro: nó alvo não encontrado
    if finalLista == inicioLista:                   # Lista com nó único
        lista = None                                # Remove o nó
        return 0                                    # Lista agora está vazia, saída normal
    if noAnterior == finalLista:                    # Remover nó inicial da lista
        finalLista.proximo = inicioLista.proximo
        inicioLista = finalLista.proximo
    elif noAnterior.proximo == finalLista:          # Remover nó final da lista
        finalLista = noAnterior
        noAnterior.proximo = inicioLista
    else:                                           # Remoção de um nó que não está nas pontas
        noAtual = noAnterior.proximo
        noAnterior.proximo = noAtual.proximo        # Saída normal
    return 0
