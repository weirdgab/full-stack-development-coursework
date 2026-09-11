def buscaLista(k, L, n):
    i = 0
    indiceL = -1
    while i < n:
        if L[i] == k:   # Nó encontrado
            indiceL = i  # Salva o índice
            i = n + 1   # Sair do laço
        i = i + 1       # Segue a procura
    return indiceL
