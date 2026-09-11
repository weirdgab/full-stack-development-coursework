# Remoção direta
def removeL(k, L, n):
    i = 0                     # Início da busca do nó
    posRemocao = -1
    while (i < n):
        if L[i] == k:
            posRemocao = i    # Chave encontrada
            i = n + 1         # Sair do laço
        else:
            i = i + 1         # Continuar busca
    if i == n:
        return -1         # Erro, chave não existe
        # Final da busca do nó
    i = posRemocao        # Início do ajuste da lista
    while (i < n - 1):
        Lista[i] = Lista[i + 1]   # Puxa cada nó posterior 1 posição
        i = i + 1
    L.pop(n - 1)                  # Ajusta o tamanho da lista
    return posRemocao             # Saída normal da função


# Testando remoção
nomes = ['João', 'Maria', 'Ana', 'Arthur']

i = removeL('Arthur', nomes, len(nomes))
print(nomes)
